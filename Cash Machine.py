#Pin has already been created and given starting balance 
pin = 1111
bal = 500
login = 1111
transactions = []

answer = input("Do you have an account? Y/N ")
if answer == "Y":
   login = int(input("Please input your pin: "))
if login == pin:
    print("You have signed in")

if answer == "N":
    print("An account has been created for you, your pin is 1111")
login = int(input("Please enter your new pin "))

if login == pin:
    print("You have now signed in")

else:
    print("Please retry answering either Y or N")
    

option = input(
        "\nWhat action would you like to perform?:\n"
        "1. Check balance\n"
        "2. Deposit money\n"
        "3. Withdraw money\n"
        "4. Transaction history\n"
        "Please input one of the following options: ")
    
if option == "1": 
        print("Your balance is:", bal)

if option == "2":
    deposit = int(input("How much would you like to deposit? "))
    print("Your new balance is:", bal + deposit)
    transactions.append(f"Deposited: +{deposit}, New balance: {bal}")

if option == "3":
    withdraw = int(input("How much would you like to withdraw? "))
    print("Your new balance is:", bal - withdraw)
    transactions.append(f"Withdrew: -{withdraw}, New balance: {bal}")
    if withdraw > bal:
        print("You do not have enough money in your account to take out, your current balance is:", bal)             

if option == 4:
    for transaction in transactions:
        print(transaction)

