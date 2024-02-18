#user input and Data Management
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description, category):
        self.expenses.append({"amount": amount, "description": description, "category": category})

tracker = ExpenseTracker()

amount = float(input("Enter amount spent: "))
description = input("Enter a brief description: ")
category = input("Enter expense category: ")
tracker.add_expense(amount, description, category)

#Expense category
class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, amount, description, category):
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append({"amount": amount, "description": description})


#Data Analysis
class ExpenseTracker:
    # Existing code...
    
    def get_monthly_summary(self, month):
        monthly_total = 0
        for expense in self.expenses:
            for item in self.expenses[expense]:
                # Assuming item is a dictionary containing 'amount' and 'description' keys
                monthly_total += item["amount"]
        return monthly_total


#User-Friendly Interface:
def main():
    while True:
        print("1. Add Expense")
        print("2. View Monthly Summary")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount spent: "))
            description = input("Enter a brief description: ")
            category = input("Enter expense category: ")
            tracker.add_expense(amount, description, category)
        elif choice == "2":
            month = input("Enter month (e.g., January, February): ")
            total = tracker.get_monthly_summary(month)
            print(f"Total expenses for {month}: ${total}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    main()

#Exception handling:
try:
    amount = float(input("Enter amount spent: "))
except ValueError:
    print("Invalid amount. Please enter a numeric value.")


