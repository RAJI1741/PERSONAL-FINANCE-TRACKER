import streamlit as st
from datetime import date

st.set_page_config(page_title="Finance Tracker", layout="centered")
st.title("💰 Personal Finance Tracker (Debug-Safe)")

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
        st.session_state.transactions.append(
            ("Income", amount, category, d)
        )
        st.success("✅ Income added")

# -----------------------------
# Add Expense
# -----------------------------
elif menu == "Add Expense":
    st.subheader("➖ Add Expense")

    amount = st.number_input("Expense Amount", min_value=1.0, step=100.0)
    category = st.text_input("Expense Category")
    d = st.date_input("Date", value=date.today())

    if st.button("Add Expense"):
        st.session_state.expense_total += amount
        st.session_state.transactions.append(
            ("Expense", amount, category, d)
        )
        st.success("✅ Expense added")

    # 🚨 ALERT (NO DATAFRAME, NO BUTTON DEPENDENCY)
    if st.session_state.expense_total > st.session_state.income_total:
        st.error("🚨 ALERT: Expenses are higher than Income!")

# -----------------------------
# View Report
# -----------------------------
elif menu == "View Report":
    st.subheader("📊 Financial Report")

    st.metric("Total Income", f"₹ {st.session_state.income_total}")
    st.metric("Total Expense", f"₹ {st.session_state.expense_total}")
    st.metric(
        "Net Amount",
        f"₹ {st.session_state.income_total - st.session_state.expense_total}"
    )

    if st.session_state.expense_total > st.session_state.income_total:
        st.error("🚨 ALERT: Expenses are higher than Income!")

    st.write("### Transactions")
    for t in st.session_state.transactions:
        st.write(t)
