import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Personal Finance Tracker",
    layout="centered"
)

st.title("💰 Personal Finance Tracker")

# -----------------------------
# Session State
# -----------------------------
if "income_total" not in st.session_state:
    st.session_state.income_total = 0.0

if "expense_total" not in st.session_state:
    st.session_state.expense_total = 0.0

if "transactions" not in st.session_state:
    st.session_state.transactions = []

# -----------------------------
# Sidebar Menu
# -----------------------------
menu = st.sidebar.radio(
    "Select Option",
    ["Add Income", "Add Expense", "View Report"]
)

# -----------------------------
# Add Income
# -----------------------------
if menu == "Add Income":
    st.subheader("➕ Add Income")

    amount = st.number_input(
        "Income Amount",
        min_value=1.0,
        step=100.0
    )

    category = st.text_input("Income Category")
    d = st.date_input("Date", value=date.today())

    if st.button("Add Income"):
        st.session_state.income_total += amount
        st.session_state.transactions.append({
            "Type": "Income",
            "Amount": amount,
            "Category": category,
            "Date": d
        })
        st.success("✅ Income added successfully")

# -----------------------------
# Add Expense
# -----------------------------
elif menu == "Add Expense":
    st.subheader("➖ Add Expense")

    amount = st.number_input(
        "Expense Amount",
        min_value=1.0,
        step=100.0
    )

    category = st.text_input("Expense Category")
    d = st.date_input("Date", value=date.today())

    if st.button("Add Expense"):
        # Block expense if exceeds income
        if st.session_state.expense_total + amount > st.session_state.income_total:
            st.error("🚨 Expense exceeds income! Transaction not allowed.")
        else:
            st.session_state.expense_total += amount
            st.session_state.transactions.append({
                "Type": "Expense",
                "Amount": amount,
                "Category": category,
                "Date": d
            })
            st.success("✅ Expense added successfully")

# -----------------------------
# View Report
# -----------------------------
elif menu == "View Report":
    st.subheader("📊 Financial Report")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"₹ {st.session_state.income_total:.2f}")
    col2.metric("Total Expense", f"₹ {st.session_state.expense_total:.2f}")
    col3.metric(
        "Net Amount",
        f"₹ {(st.session_state.income_total - st.session_state.expense_total):.2f}"
    )

    if not st.session_state.transactions:
        st.info("No transactions yet.")
        st.stop()

    df = pd.DataFrame(st.session_state.transactions)
    df["Date"] = pd.to_datetime(df["Date"])

    st.markdown("## 📈 Visual Insights")

    # -----------------------------
    # Income vs Expense Bar Chart
    # -----------------------------
    st.subheader("💵 Income vs Expense")

    summary_df = pd.DataFrame({
        "Type": ["Income", "Expense"],
        "Amount": [
            st.session_state.income_total,
            st.session_state.expense_total
        ]
    })

    st.bar_chart(summary_df.set_index("Type"))

    # -----------------------------
    # Expense Category Pie Chart
    # -----------------------------
    expense_df = df[df["Type"] == "Expense"]

    if not expense_df.empty:
        st.subheader("🥧 Expense Breakdown by Category")

        fig, ax = plt.subplots()
        expense_df.groupby("Category")["Amount"].sum().plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90,
            ax=ax
        )
        ax.set_ylabel("")
        st.pyplot(fig)

    # -----------------------------
    # Cash Flow Over Time
    # -----------------------------
    st.subheader("📊 Cash Flow Over Time")

    timeline_df = (
        df.pivot_table(
            index="Date",
            columns="Type",
            values="Amount",
            aggfunc="sum",
            fill_value=0
        )
        .sort_index()
    )

    st.line_chart(timeline_df)

    # -----------------------------
    # Transaction History
    # -----------------------------
    st.markdown("### 🧾 Transaction History")
    st.dataframe(df, use_container_width=True)
