

from datetime import date
import json


with open("transactions.json", "r") as f:
        data = json.load(f)

def add_transaction(transaction_type,category,amount):
            
            # transaction = {}          #This was another way of doing the same work, but it wasn't the best way. So, below is concise & better code.
            # transaction["type"] = transaction_type
            # transaction["category"] = category
            # transaction["amount"] = amount
            # transaction["date"] = date.today().isoformat()

            transaction = {
                "type": transaction_type,
                "category": category,
                "amount": amount,
                "date": date.today().isoformat()
                }
            data.append(transaction)
            
# Menu button 1 & 2:
def get_transaction_details(transaction_type):
    new_category = input("please add category: ")
    new_amount = float(input("please add amount: "))

    add_transaction(transaction_type, new_category, new_amount)

# Menu 3
def view_transactions():
            transactions_count = 0
            for i in data:
                transactions_count+=1
                print(f"___________Transaction #{transactions_count}___________")
                print(f"Date: {i["date"]}\nType: {i["type"]}\nCategory: {i["category"]}\nAmount: {i["amount"]}")

# Menu 4
def show_summary():
      income = 0
      income_count = 0
      expense = 0
      expense_count = 0
      total_transactions= 0
      for i in data:
        if i["type"] == "income": # if dictionary then access data in loop by key, or if lists then by index number i[0].
            income+=i["amount"]
            income_count+=1
        else:
            expense+=i["amount"]
            expense_count+=1
        total_transactions+=1
        
      print("====================SUMMARY====================")
      print(f"Total income is: {income} and transaction count is : {income_count}")
      print(f"Total expense is: {expense} and transaction count is : {expense_count}")
      print(f"Total transactions are: {total_transactions}")
      print(f"You current balance is: {income - expense}")
# Menu 5
def save():
       with open("transactions.json", "w") as f:
        json.dump(data,f,indent=4)

# Menu
while True:
    choice = input("""
    1- Add income
    2- Add expense
    3- View all transactions
    4- Show summary
    5- Save data
    6- Exit: 
    Choose from options: """)

    if choice == "1":
        get_transaction_details("income")

    elif choice == "2":
        get_transaction_details("expense")

    elif choice == "3":
            view_transactions()

    elif choice == "4":
          show_summary()

    elif choice == "5":
          save()
          print("Data saved successfully!")

    elif choice == "6":
            print("Program exited successfully!")
            break

    else:
      print("Invalid entry!!!")