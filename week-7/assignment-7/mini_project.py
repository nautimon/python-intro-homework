import os
import csv
from datetime import datetime

if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found")

    with open ("../data/expenses.csv") as file:
        reader = list(csv.DictReader(file))
        total = 0
        food_expenses = []

        for column in reader:
            column["amount"] = float(column["amount"])

            if column["category"]=="Food":
                    total += column["amount"]
                    food_expenses.append(column)

    with open('food_report.txt', 'w') as file:
        now = datetime.now()
        today = now.strftime("%B %d, %Y")

        file.write(f"Food Expense Report - generated {today}\n")

        for expense in food_expenses:
            file.write(f"{expense["date"]}: ${expense["amount"]:.2f}\n")

        file.write(f"Total: ${total:.2f}\n")
else:
    print("expenses.csv not found")