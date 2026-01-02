import streamlit as st
import pandas as pd
from datetime import datetime, date
import uuid
import altair as alt

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
if "transactions" not in st.session_state:
    st.session_state.transactions = []

if "income_total" not in st.session_state:
    st.session_state.income_total = 0.0

if "expense_total" not in st.session_state:
    st.session_state.expense_total = 0.0

# -----------------------------
# Sidebar Menu
# -----------------------------
menu = st.sidebar.radio(
    "📌 Menu",
    ["Add Transaction", "View Report"]
)

# -----------------------------
# Add Unified Transaction
# -----------------------------
if menu == "Add Transaction":
    st.subheader("➕ Add New Transaction")

    with st.form("transaction_form"):
        txn_id = str(uuid.uuid4())[:8]
        txn_date = st.date_input("📅 Date", value=date.today())
        txn_time = datetime.now().strftime("%H:%M:%S")

        st.markdown("### 💵 Income (optional)")
        income_amount = st.number_input(
            "Income Amount",
            min_value=0.0,
            step=100.0
        )
        income_category = st.text_input("Income Source")

        st.markdown("### ➖ Expense (optional)")
        expense_amount = st.number_input(
            "Expense Amount",
            min_value=0.0,
            step=100.0
        )
        expense_category = st.text_input("Expense Category")

        submit = st.form_submit_button("✅ Submit Transaction")

    if submit:
        if income_amount == 0 and expense_amount == 0:
            st.error("🚨 Enter at least income or expense")
            st.stop()

        if expense_amount > 0 and (
            st.session_state.expense_total + expense_amount >
            st.session_state.income_total + income_amount
        ):
            st.error("🚨 Expense exceeds available income")
            st.stop()

        # Save Income
        if income_amount > 0:
            st.session_state.transactions.append({
                "Transaction ID": txn_id,
                "Type": "Income",
                "Amount": income_amount,
                "Category": income_category,
                "Date": txn_date,
                "Time": txn_time
            })
            st.session_state.income_total += income_amount

        # Save Expense
        if expense_amount > 0:
            st.session_state.transactions.append({
                "Transaction ID": txn_id,
                "Type": "Expense",
                "Amount": expense_amount,
                "Category": expense_category,
                "Date": txn_date,
                "Time": txn_time
            })
            st.session_state.expense_total += expense_amount

        st.success("🎉 Transaction recorded successfully")

        # Instant Download
        df = pd.DataFrame(st.session_state.transactions)
        latest_txn = df[df["Transaction ID"] == txn_id]

        st.markdown("### ⬇️ Download This Transaction")
        st.download_button(
            "Download Transaction CSV",
            latest_txn.to_csv(index=False),
            file_name=f"transaction_{txn_id}.csv",
            mime="text/csv"
        )

# -----------------------------
# View Report
# -----------------------------
elif menu == "View Report":
    st.subheader("📊 Financial Dashboard")

    net = st.session_state.income_total - st.session_state.expense_total

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"₹ {st.session_state.income_total:.2f}")
    col2.metric("Total Expense", f"₹ {st.session_state.expense_total:.2f}")
    col3.metric("Net Savings", f"₹ {net:.2f}")

    if not st.session_state.transactions:
        st.info("No transactions yet.")
        st.stop()

    df = pd.DataFrame(st.session_state.transactions)
    df["Date"] = pd.to_datetime(df["Date"])

    # -----------------------------
    # Bar Chart
    # -----------------------------
    st.markdown("### 📈 Income vs Expense")
    summary = df.groupby("Type")["Amount"].sum().reset_index()
    st.bar_chart(summary.set_index("Type"))

    # -----------------------------
    # Pie Chart (Expenses)
    # -----------------------------
    expense_df = df[df["Type"] == "Expense"]

    if not expense_df.empty:
        st.markdown("### 🥧 Expense Breakdown by Category")

        pie_data = (
            expense_df.groupby("Category")["Amount"]
            .sum()
            .reset_index()
        )

        pie_chart = alt.Chart(pie_data).mark_arc().encode(
            theta=alt.Theta(field="Amount", type="quantitative"),
            color=alt.Color(field="Category", type="nominal"),
            tooltip=["Category", "Amount"]
        )

        st.altair_chart(pie_chart, use_container_width=True)

    # -----------------------------
    # Transaction History
    # -----------------------------
    st.markdown("### 🧾 Transaction History")
    st.dataframe(
        df.sort_values(by=["Date", "Time"], ascending=False),
        use_container_width=True
    )

    # -----------------------------
    # Download Full Report
    # -----------------------------
    st.markdown("### ⬇️ Download Full Report")
    st.download_button(
        "Download Full CSV",
        df.to_csv(index=False),
        file_name="full_finance_report.csv",
        mime="text/csv"
    )
