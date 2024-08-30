expenses = []

def removeExpense():
    listExpenses()
    print("What expense would you like to remove (enter the expense number)?")
    try:
        expenseToRemove = int(input("> "))
        if 0 <= expenseToRemove < len(expenses):
            del expenses[expenseToRemove]
            print("Expense removed successfully.")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def addExpense():
    print("Input the cost of this expense")
    amountToAdd = input("> ")
    
    print("What category was this expense?")
    category = input("> ")
    
    print("What date was this expense? (YYYY-MM-DD)")
    date = input("> ")

    expense = {'amount': float(amountToAdd), 'category': category, 'date': date}
    expenses.append(expense)
    print("Expense added successfully.")

def printMenu():
    print("\nChoose from the following options:")
    print("1. Add New Expense")
    print("2. Remove Expense")
    print("3. List All Expenses")
    print("4. Quit")

def listExpenses():
    if not expenses:
        print("\nNo expenses recorded.")
        return

    total_cost = sum(expense['amount'] for expense in expenses)
    
    print("\nHere is a list of your expenses:")
    print("\n================================")
    
    for i, expense in enumerate(expenses):
        print("#" + str(i), " • Amount:", expense['amount'], " • Category:",
              expense['category'], 
              " • Date:", expense['date'])
    
    print("\nTotal Cost of All Expenses:", total_cost)

if __name__ == "__main__":
    while True:
        printMenu()
        optionSelect = input("> ")

        if optionSelect == "1":
            addExpense()
        elif optionSelect == "2":
            removeExpense()
        elif optionSelect == "3":
            listExpenses()
        elif optionSelect == "4":
            print("Exiting the expense tracker... Goodbye!")
            break
        else:
            print("Invalid input, please try again.")
