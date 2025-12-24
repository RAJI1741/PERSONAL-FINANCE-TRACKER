# 💰 Personal Finance Tracker (Streamlit App)

A simple and interactive **Personal Finance Tracker** built using **Python** and **Streamlit**.  
This application helps users record **income and expenses**, track their **financial balance**, and view a **detailed financial report with transaction history**.

---

## 🚀 Features

- ➕ Add **Income** with amount, category, and date  
- ➖ Add **Expense** with amount, category, and date  
- 📊 View **Financial Report**
  - Total Income
  - Total Expense
  - Net Amount (Income − Expense)
- 🧾 View **complete transaction history**
- 📅 Date handling using proper date input
- 💾 Uses **Streamlit Session State** to persist data during runtime
- 📈 Clean and user-friendly UI

---

## 🛠️ Technologies Used

- **Python 3**
- **Streamlit**
- **Pandas**
- **Object-Oriented Programming (OOP)** concepts

---

## 📂 Project Structure
├── personal-finance-tracker.py # Main Streamlit application
├── README.md # Project documentation



---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/personal-finance-tracker.git
cd personal-finance-tracker
```


pip install streamlit pandas

streamlit run personal-finance-tracker.py


📊 Application Screens
🔹 Add Income
Enter income amount
Select category (Salary, Bonus, etc.)
Choose date
🔹 Add Expense
Enter expense amount
Select category (Food, Rent, Travel, etc.)
Choose date
🔹 View Report
Displays:
Total Income
Total Expense
Net Amount
Shows full transaction history in a table



Net Amount Logic

Net Amount = Total Income − Total Expense
This value is calculated fresh for every report, ensuring accurate financial summaries.




