# Expense Tracker Project 

expensesList = [] #list of expenses in form of dictionary 
print(" Welcome to Expense Tracker : ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice= int(input("Please Enter Your Choice : "))

#ADD Expense
    if(choice == 1):
        date= input("Enter the date: ")
        category= input("Enter the category (Food, Travel, Makeup, Books): ")
        description= input("Enter any extra information: ")
        amount= float(input("Enter the amount: "))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print(" \n DONE. Expense is added succesfully")

# 2. VIEW ALL EXPENSES 
    elif(choice == 2):
        if( len(expensesList)==0 ):
            print("No Expenses Added. ")
        else:
           print("===== This is your total expense ======")
           count= 1
           for eachexpense in expensesList:
                print(f"expense Number {count} -> {eachexpense["date"]}, {eachexpense["category"]}, {eachexpense["description"]}, {eachexpense["amount"]} ")
                count= count+1

# 3. View TOtal Spending 
    elif(choice == 3):
        total= 0
        for eachexpense in expensesList:
            total = total + eachexpense["amount"]

        print("\n TOTAL expense = ", total)

#4. EXIT 
    elif(choice == 4):
        print("THANKYOU FOR USING OUR SYSTEM")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")