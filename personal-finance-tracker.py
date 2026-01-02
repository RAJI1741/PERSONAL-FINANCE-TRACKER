import streamlit as st
import pandas as pd
from datetime import date

# -----------------------------
# Classes
# -----------------------------
class Transaction:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date


class Account:
    def __init__(self):
        self.transactions = []

    def add(self, t_type, amount, category, date):
        if amount <= 0 or not category.strip():
            return False

        self.transactions.append({
            "Type": t_type,
            "Amount": amount,
            "Category": category,
            "Date": date
        })
        return True


# -----------------------------
# Session State
# -----------------------------
if "account" not in st.session_state:
    st.session_state.account = Account()


# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="Personal Finance Tracker", layout="centered")
st.title("💰 Personal Finance Tracker")

menu = st.sidebar.radio("Select Option", ["Add Income", "Add Expense", "View Report"])


# -----------------------------
# Helper (IMPORTANT)
# -----------------------------
def show_alert_if_needed():
    if not st.session_state.account.transactions:
        return

    df = pd.DataFrame(st.session_state.account.transactions)
    income = df[df["Type"] == "Income"]["Amount"].sum()
    expense = df[df["Type"] == "Expense"]["Amount"].sum()

    if expense > income:
        st.error("🚨 Alert! Your expenses are higher than your income!")


# -----------------------------
# Add Income
# -----------------------------
if menu == "Add Income":
    st.subheader("➕ Add Income")

    amount = st.number_input("Income Amount", min_value=1.0, step=100.0)
    category = st.text_input("Income Category")
    d = st.date_input("Date", value=date.today())

    if st.button("Add Income"):
        if st.session_state.account.add("Income", amount, category, d):
            st.success("✅ Income added")
        else:
            st.error("❌ Invalid input")

    show_alert_if_needed()


# -----------------------------
# Add Expense
# -----------------------------
elif menu == "Add Expense":
    st.subheader("➖ Add Expense")

    amount = st.number_input("Expense Amount", min_value=1.0, step=100.0)
    category = st.text_input("Expense Category")
    d = st.date_input("Date", value=date.today())

    if st.button("Add Expense"):
        if st.session_state.account.add("Expense", amount, category, d):
            st.success("✅ Expense added")
        else:
            st.error("❌ Invalid input")

    # 🔥 ALWAYS CHECK AFTER RERUN
    show_alert_if_needed()


# -----------------------------
# View Report
# -----------------------------
elif menu == "View Report":
    st.subheader("📊 Financial Report")

    if not st.session_state.account.transactions:
        st.warning("⚠️ No transactions")
    else:
        df = pd.DataFrame(st.session_state.account.transactions)

        income = df[df["Type"] == "Income"]["Amount"].sum()
        expense = df[df["Type"] == "Expense"]["Amount"].sum()
        net = income - expense

        c1, c2, c3 = st.columns(3)
        c1.metric("Total Income", f"₹ {income}")
        c2.metric("Total Expense", f"₹ {expense}")
        c3.metric("Net Amount", f"₹ {net}")

        show_alert_if_needed()

        st.dataframe(df, use_container_width=True)
