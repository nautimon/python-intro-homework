import os
files = os.getcwd()
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
print(files)
path = os.path.join("..", "data", "expenses.csv")
print(path)