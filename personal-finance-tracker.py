import streamlit as st
import pandas as pd
from datetime import date

# -----------------------------
# Transaction Classes
# -----------------------------
class Transaction:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def apply(self, account):
        pass


class Income(Transaction):
    def apply(self, account):
        account.balance += self.amount


class Expense(Transaction):
    def apply(self, account):
        account.balance -= self.amount


# -----------------------------
# Account Class
# -----------------------------
class Account:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    def add_transaction(self, transaction, t_type):
        if transaction.amount <= 0 or not transaction.category.strip():
            return False

        transaction.apply(self)
        self.transactions.append({
            "Type": t_type,
            "Amount": transaction.amount,
            "Category": transaction.category,
            "Date": transaction.date
        })
        return True


# -----------------------------
# Session State Initialization
# -----------------------------
if "account" not in st.session_state:
    st.session_state.account = Account()


# -----------------------------
# App UI
# -----------------------------
st.set_page_config(page_title="Personal Finance Tracker", layout="centered")

st.title("💰 Personal Finance Tracker")

menu = st.sidebar.radio(
    "Select Option",
    ["Add Income", "Add Expense", "View Report"]
)

# -----------------------------
# Add Income
# -----------------------------
if menu == "Add Income":
    st.subheader("➕ Add Income")

    amount = st.number_input("Income Amount", min_value=0.0, step=100.0)
    category = st.text_input("Income Category (Salary, Bonus, etc.)")
    trans_date = st.date_input("Date", value=date.today())

    if st.button("Add Income"):
        income = Income(amount, category, trans_date)
        success = st.session_state.account.add_transaction(income, "Income")

        if success:
            st.success("✅ Income added successfully")
        else:
            st.error("❌ Amount must be greater than zero and category cannot be empty")


# -----------------------------
# Add Expense
# -----------------------------
elif menu == "Add Expense":
    st.subheader("➖ Add Expense")

    amount = st.number_input("Expense Amount", min_value=0.0, step=100.0)
    category = st.text_input("Expense Category (Food, Rent, Travel, etc.)")
    trans_date = st.date_input("Date", value=date.today())

    if st.button("Add Expense"):
    expense = Expense(amount, category, trans_date)
    success = st.session_state.account.add_transaction(expense, "Expense")

    if success:
        st.success("✅ Expense added successfully")

        # 🔔 INSTANT ALERT CHECK
        df = pd.DataFrame(st.session_state.account.transactions)
        total_income = df[df["Type"] == "Income"]["Amount"].sum()
        total_expense = df[df["Type"] == "Expense"]["Amount"].sum()

        if total_expense > total_income:
            st.error("🚨 Alert! Your expenses are now higher than your income!")

    else:
        st.error("❌ Amount must be greater than zero")


# -----------------------------
# View Report
# -----------------------------
elif menu == "View Report":
    st.subheader("📊 Financial Report")

    if not st.session_state.account.transactions:
        st.warning("⚠️ No transactions available")
    else:
        df = pd.DataFrame(st.session_state.account.transactions)

        total_income = df[df["Type"] == "Income"]["Amount"].sum()
        total_expense = df[df["Type"] == "Expense"]["Amount"].sum()

        net_amount = total_income - total_expense

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Income", f"₹ {total_income}")
        col2.metric("Total Expense", f"₹ {total_expense}")
        col3.metric("Net Amount", f"₹ {net_amount}")

        # 🚨 ALERT CONDITION
        if total_expense > total_income:
            st.error("🚨 Alert! Your expenses are higher than your income. Please control spending!")

        st.markdown("### 🧾 Transaction History")
        st.dataframe(df, use_container_width=True)

