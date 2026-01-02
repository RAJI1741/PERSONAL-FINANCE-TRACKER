import streamlit as st
import pandas as pd
from datetime import date
import uuid

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

        # Validate expense
        if expense_amount > 0 and (
            st.session_state.expense_total + expense_amount >
            st.session_state.income_total + income_amount
        ):
            st.error("🚨 Expense exceeds available income")
            st.stop()

        # Save income
        if income_amount > 0:
            st.session_state.transactions.append({
                "Transaction ID": txn_id,
                "Type": "Income",
                "Amount": income_amount,
                "Category": income_category,
                "Date": txn_date
            })
            st.session_state.income_total += income_amount

        # Save expense
        if expense_amount > 0:
            st.session_state.transactions.append({
                "Transaction ID": txn_id,
                "Type": "Expense",
                "Amount": expense_amount,
                "Category": expense_category,
                "Date": txn_date
            })
            st.session_state.expense_total += expense_amount

        st.success("🎉 Transaction recorded successfully")

        # -----------------------------
        # Instant Download
        # -----------------------------
        df = pd.DataFrame(st.session_state.transactions)
        latest_txn = df[df["Transaction ID"] == txn_id]

        st.markdown("### ⬇️ Download Transaction Report")
        st.download_button(
            label="Download This Transaction (CSV)",
            data=latest_txn.to_csv(index=False),
            file_name=f"transaction_{txn_id}.csv",
            mime="text/csv"
        )

# -----------------------------
# View Report
# -----------------------------
elif menu == "View Report":
    st.subheader("📊 Financial Summary")

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

    st.markdown("### 📈 Overview")
    summary = df.groupby("Type")["Amount"].sum()
    st.bar_chart(summary)

    st.markdown("### 🧾 All Transactions")
    st.dataframe(df, use_container_width=True)

    st.markdown("### ⬇️ Download Full Report")
    st.download_button(
        label="Download Full Report (CSV)",
        data=df.to_csv(index=False),
        file_name="full_finance_report.csv",
        mime="text/csv"
    )
