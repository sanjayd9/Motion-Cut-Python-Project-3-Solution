import os
import datetime

# Function to display the menu
def display_menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

# Function to add an expense
def add_expense():
    amount = float(input("Enter the expense amount: "))
    description = input("Enter a description: ")

    # Get the current date and time
    current_datetime = datetime.datetime.now()
    date_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Append the expense details to the file
    with open("expenses.txt", "a") as file:
        file.write(f"{date_string} - {amount:.2f} - {description}\n")

    print("Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("Date                | Amount | Description")
                print("-----------------------------------------")
                for expense in expenses:
                    print(expense, end="")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Main function
def main():
    # Create the expenses file if it doesn't exist
    if not os.path.exists("expenses.txt"):
        open("expenses.txt", "w").close()

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-3).\n")

if __name__ == "__main__":
    main()
