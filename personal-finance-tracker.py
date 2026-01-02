import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Personal Finance Tracker", layout="centered")
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
# Sidebar
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

    amount = st.number_input("Income Amount", min_value=1.0, step=100.0)
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

    amount = st.number_input("Expense Amount", min_value=1.0, step=100.0)
    category = st.text_input("Expense Category")
    d = st.date_input("Date", value=date.today())

    if st.button("Add Expense"):

        # ❌ Block expense if it exceeds income
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
    col1.metric("Total Income", f"₹ {st.session_state.income_total}")
    col2.metric("Total Expense", f"₹ {st.session_state.expense_total}")
    col3.metric(
        "Net Amount",
        f"₹ {st.session_state.income_total - st.session_state.expense_total}"
    )

    # 🚨 Warning (no operation, only alert)
    if st.session_state.expense_total > st.session_state.income_total:
        st.error("🚨 Alert! Expenses are higher than income.")

    st.markdown("### 🧾 Transaction History")

    if st.session_state.transactions:
        df = pd.DataFrame(st.session_state.transactions)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No transactions yet.")
