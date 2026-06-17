Project Overview

The Personal Finance Manager is a command-line based Python application designed to help users track and manage their daily expenses 
efficiently. The project allows users to record expenses, store them persistently using CSV files, generate financial reports, and 
back up data.
This project is built using core Python concepts such as classes, file handling, CSV module, error handling, and modular programming. 
It is suitable for academic submission, Python practice, and viva/interview preparation.

Features

Add new expenses with date, category, amount, and description
View all recorded expenses
Category-wise expense summary
Monthly expense report (total & average)
Search expenses by category or description
CSV-based data persistence
Data backup functionality
Input validation and error handling
Modular and clean project structure

Complete Python Personal Finance Manager/
│
├── main.py # Program entry point
├── menu.py # Menu-driven user interface
├── expense.py # Expense class definition
├── file_manager.py # CSV file handling & backup
├── reports.py # Expense calculations & reports
├── utils.py # Validation and helper functions
│
├── data/
│ ├── expenses.csv # Stores expense records
│ └── expenses_backup.csv
│
└── reports/
└── monthly_report.txt
