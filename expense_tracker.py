import pandas as pd
import csv
from datetime import datetime, date

FILE_NAME = "expenses.csv"
CATEGORIES = ['Food', 'Transport', 'Entertainment', 'Utilities']

def add_expense():
    category = input("Enter category (Food, Transport, Entertainment, Utilities): ").strip()
    if category not in CATEGORIES:
        print("Invalid category. Please choose from Food, Transport, Entertainment, Utilities.")
        return

    try:
        amount = float(input(f"Enter the amount spent on {category}: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    expense_date = input("Enter the date (YYYY-MM-DD) or press Enter to use today's date: ").strip()
    if not expense_date:
        expense_date = date.today().isoformat()
    try:
        datetime.strptime(expense_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    data_list = [[expense_date, category, amount]]
    df = pd.DataFrame(data_list, columns=['Date', 'Category', 'Amount'])
    df.to_csv(FILE_NAME, mode='a', header=not pd.io.common.file_exists(FILE_NAME), index=False)
    print(f"Expense recorded: {expense_date}, {category}, {amount}")


def view_summary():
    try:
        expenses = []
        with open(FILE_NAME, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["Amount"] = float(row["Amount"])
                row["Date"] = datetime.strptime(row["Date"], "%Y-%m-%d")
                expenses.append(row)
    except FileNotFoundError:
        print("No expenses recorded yet.")
        return

    filter_choice = input("Do you want to filter by date range? (yes/no): ").strip().lower()
    if filter_choice == "yes":
        start_date_input = input("Enter start date (YYYY-MM-DD): ").strip()
        end_date_input = input("Enter end date (YYYY-MM-DD): ").strip()
        try:
            start_date = datetime.strptime(start_date_input, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_input, "%Y-%m-%d")
            expenses = [e for e in expenses if start_date <= e["Date"] <= end_date]
        except ValueError:
            print("Invalid date format. Showing all data.")

    summary = {}
    for expense in expenses:
        cat = expense["Category"]
        summary[cat] = summary.get(cat, 0) + expense["Amount"]

    print("\nExpense Summary:")
    for cat, total in summary.items():
        print(f"{cat}: {total:.2f}")
    print("\n")


def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
