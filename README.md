## Expense Tracker CLI (Python)

A simple command-line based Expense Tracker built using Python.
This project focuses on clean architecture, separation of concerns, and proper development practices.

---

## 📌 Features

* Add expense with amount, category, and description
* View all expenses in formatted output
* Input validation for user entries
* JSON-based data persistence
* Indexed display for easy readability
* Placeholder support for upcoming features:

  * Delete Expense
  * Total Expense Calculation

---

## 🧱 Project Structure

```
expense-tracker/
│
├── app/
│   ├── main.py        # Handles CLI interaction (input/output)
│   ├── expense.py     # Business logic (create & format expenses)
│   ├── storage.py     # JSON read/write operations
│   └── utils.py       # Helper functions (reserved for future use)
│
├── data.json          # Stores expense data
├── .gitignore
├── README.md
```

---

## ⚙️ Architecture Principles

This project strictly follows separation of concerns:

* `main.py` → User interaction only
* `expense.py` → Data creation & formatting logic
* `storage.py` → Data persistence (JSON handling)

No file handling or input/output logic is mixed across modules.

---

## 🚀 Getting Started

### 1. Clone the repository

```
git clone <your-repo-url>
cd expense-tracker
```

---

### 2. (Optional) Create virtual environment

```
python -m venv venv
```

Activate:

* Windows:

```
venv\Scripts\activate
```

---

### 3. Initialize data file

Ensure `data.json` contains:

```
[]
```

---

### 4. Run the application

```
python app/main.py
```

---

## 🧾 Example Output

```
Your Expenses:
1. ₹10.0/- | Food | Vadapav
2. ₹20.0/- | Travel | Metro
```

---

## ⚠️ Known Limitations

* No delete functionality yet
* No total expense calculation
* No persistent unique IDs for expenses

---

## 🔮 Future Improvements

* Delete expense by index
* Total expense calculation
* Unique ID system for each expense
* Data validation enhancements
* Export to CSV

---

## 🧠 Learning Goals

This project is built to practice:

* Clean code structure
* Modular design
* Git & GitHub workflow
* CLI-based application development

---

## 📄 License

This project is for educational purposes.
