# # # -----------------------------
# # # Base class for all transactions
# # # -----------------------------
# # class Transaction:
# #     def __init__(self, amount, category, date):
# #         # Amount of money involved in the transaction
# #         self.amount = amount
# #         # Category of transaction (e.g., Salary, Food, Rent)
# #         self.category = category
# #         # Date of transaction
# #         self.date = date

# #     # This method will be overridden in child classes
# #     # It defines how a transaction affects the account balance
# #     def apply(self, account):
# #         pass


# # # -----------------------------
# # # Income class (adds money)
# # # -----------------------------
# # class Income(Transaction):
# #     def apply(self, account):
# #         # Increase account balance by income amount
# #         account._balance += self.amount


# # # -----------------------------
# # # Expense class (deducts money)
# # # -----------------------------
# # class Expense(Transaction):
# #     def apply(self, account):
# #         # Decrease account balance by expense amount
# #         account._balance -= self.amount


# # # -----------------------------
# # # Account class to manage balance and transactions
# # # -----------------------------
# # class Account:
# #     def __init__(self):
# #         # Private variable to store account balance
# #         self._balance = 0.0
# #         # List to store all income and expense transactions
# #         self._transactions = []

# #     # Adds a transaction to the account
# #     def add_transaction(self, transaction):
# #         # Validate that amount is positive
# #         if transaction.amount <= 0:
# #             print("Amount must be positive")
# #             return

# #         # Apply the transaction (income or expense)
# #         transaction.apply(self)

# #         # Store the transaction in history
# #         self._transactions.append(transaction)

# #     # Returns current account balance
# #     def get_balance(self):
# #         return self._balance

# #     # Returns list of all transactions
# #     def get_transactions(self):
# #         return self._transactions


# # # -----------------------------
# # # Report generator class
# # # -----------------------------
# # class ReportGenerator:
# #     def generate_report(self, account):
# #         # Calculate total income
# #         income = sum(
# #             t.amount for t in account.get_transactions()
# #             if isinstance(t, Income)
# #         )

# #         # Calculate total expenses
# #         expense = sum(
# #             t.amount for t in account.get_transactions()
# #             if isinstance(t, Expense)
# #         )

# #         # Display financial summary
# #         print("\n----- Financial Report -----")
# #         print(f"Total Income   : ₹{income}")
# #         print(f"Total Expense  : ₹{expense}")
# #         print(f"Net Savings    : ₹{account.get_balance()}")


# # # -----------------------------
# # # Display menu options to user
# # # -----------------------------
# # def display_menu():
# #     print("\nPersonal Finance Tracker")
# #     print("1. Add Income")
# #     print("2. Add Expense")
# #     print("3. View Report")
# #     print("4. Exit")


# # # -----------------------------
# # # Main function (program execution starts here)
# # # -----------------------------
# # def main():
# #     # Create account object
# #     account = Account()

# #     # Create report generator object
# #     report = ReportGenerator()

# #     # Run menu until user exits
# #     while True:
# #         display_menu()
# #         choice = input("Enter your choice: ")

# #         # Add income
# #         if choice == "1":
# #             amount = float(input("Enter income amount: "))
# #             category = input("Enter category: ")
# #             date = input("Enter date (DD-MM-YYYY): ")
# #             account.add_transaction(Income(amount, category, date))

# #         # Add expense
# #         elif choice == "2":
# #             amount = float(input("Enter expense amount: "))
# #             category = input("Enter category: ")
# #             date = input("Enter date (DD-MM-YYYY): ")
# #             account.add_transaction(Expense(amount, category, date))

# #         # View financial report
# #         elif choice == "3":
# #             report.generate_report(account)

# #         # Exit application
# #         elif choice == "4":
# #             print("Thank you for using Personal Finance Tracker")
# #             break

# #         # Invalid menu choice
# #         else:
# #             print("Invalid choice. Try again.")


# # # -----------------------------
# # # Entry point of the program
# # # -----------------------------
# # if __name__ == "__main__":
# #     main()



# # -----------------------------
# # Base class for all transactions
# # -----------------------------
# class Transaction:
#     def __init__(self, amount, category, date):
#         self.amount = amount
#         self.category = category
#         self.date = date

#     def apply(self, account):
#         pass


# # -----------------------------
# # Income class
# # -----------------------------
# class Income(Transaction):
#     def apply(self, account):
#         account._balance += self.amount


# # -----------------------------
# # Expense class
# # -----------------------------
# class Expense(Transaction):
#     def apply(self, account):
#         account._balance -= self.amount


# # -----------------------------
# # Account class
# # -----------------------------
# class Account:
#     def __init__(self):
#         self._balance = 0.0
#         self._transactions = []

#     def add_transaction(self, transaction):
#         if transaction.amount <= 0:
#             print("❌ Amount must be greater than zero.")
#             return

#         transaction.apply(self)
#         self._transactions.append(transaction)
#         print("✅ Transaction added successfully.")

#     def get_balance(self):
#         return self._balance

#     def get_transactions(self):
#         return self._transactions


# # -----------------------------
# # Report Generator
# # -----------------------------
# class ReportGenerator:
#     def generate_report(self, account):
#         if not account.get_transactions():
#             print("\n⚠️ No transactions available to generate report.")
#             return

#         income = sum(t.amount for t in account.get_transactions() if isinstance(t, Income))
#         expense = sum(t.amount for t in account.get_transactions() if isinstance(t, Expense))

#         print("\n========== Financial Report ==========")
#         print(f"Total Income   : ₹{income}")
#         print(f"Total Expense  : ₹{expense}")
#         print(f"Net Savings    : ₹{account.get_balance()}")
#         print("=====================================")


# # -----------------------------
# # Display Menu
# # -----------------------------
# def display_menu():
#     print("\n📌 Personal Finance Tracker")
#     print("1️⃣  Add Income")
#     print("2️⃣  Add Expense")
#     print("3️⃣  View Report")
#     print("4️⃣  Exit")


# # -----------------------------
# # Safe input for amount
# # -----------------------------
# def get_valid_amount():
#     while True:
#         try:
#             amount = float(input("Enter amount: "))
#             return amount
#         except ValueError:
#             print("❌ Please enter a valid numeric amount.")


# # -----------------------------
# # Main Program
# # -----------------------------
# def main():
#     account = Account()
#     report = ReportGenerator()

#     print("💰 Welcome to Personal Finance Tracker")

#     while True:
#         display_menu()
#         choice = input("Enter your choice (1-4): ").strip()

#         if choice == "1":
#             print("\n➕ Add Income")
#             amount = get_valid_amount()
#             category = input("Enter category: ")
#             date = input("Enter date (DD-MM-YYYY): ")
#             account.add_transaction(Income(amount, category, date))

#         elif choice == "2":
#             print("\n➖ Add Expense")
#             amount = get_valid_amount()
#             category = input("Enter category: ")
#             date = input("Enter date (DD-MM-YYYY): ")
#             account.add_transaction(Expense(amount, category, date))

#         elif choice == "3":
#             report.generate_report(account)

#         elif choice == "4":
#             print("\n👋 Thank you for using Personal Finance Tracker")
#             break

#         else:
#             print("❌ Invalid choice. Please select between 1 and 4.")


# # -----------------------------
# # Entry Point
# # -----------------------------
# if __name__ == "__main__":
#     main()




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
        if transaction.amount <= 0:
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
            st.error("❌ Amount must be greater than zero")


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

        # ✅ Net amount calculated freshly for report
        net_amount = total_income - total_expense

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Income", f"₹ {total_income}")
        col2.metric("Total Expense", f"₹ {total_expense}")
        col3.metric("Net Amount", f"₹ {net_amount}")

        st.markdown("### 🧾 Transaction History")
        st.dataframe(df, use_container_width=True)


