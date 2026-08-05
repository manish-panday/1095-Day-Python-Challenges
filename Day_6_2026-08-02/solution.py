customer_name = input("Enter your name: ")
current_account_balance = float(input("Enter your current account balance: "))
withdrawal_amount = float(input("Enter an amount for withdrawal: "))
status = ""

if withdrawal_amount > 0:
    if withdrawal_amount < current_account_balance:
        status = "Sucessful Withdrawal"
    else: 
        status = "Insufficient balance"
else: 
    status = "Invalid withdrawal amount."

if status == "Invalid withdrawal amount.":
    print("Invalid Amount")
    print("========== ATM RECEIPT ==========")
    print()
    print(f"Customer: {customer_name}")
    print()
    print(f"Withdrawal Amount: {withdrawal_amount}")
    print()
    print(f"Status: {status}")
    print()
    print("=================================")
elif status == "Insufficient balance":
    print("Insufficient Balance")
    print("========== ATM RECEIPT ==========")
    print()
    print(f"Customer: {customer_name}")
    print()
    print(f"Current Balance: {current_account_balance}")
    print()
    print(f"Withdrawal Amount: {withdrawal_amount}")
    print()
    print(f"Status: {status}")
    print()
    print("=================================")
else:
    print("Sucessful Withdrawal")
    print("========== ATM RECEIPT ==========")
    print()
    print(f"Customer: {customer_name}")
    print()
    print(f"Current Balance: {current_account_balance}")
    print(f"Withdrawal Amount: {withdrawal_amount}")
    print()
    print(f"Status: {status}")
    print()
    print(f"Remaining Balance: {int(current_account_balance - withdrawal_amount)}")
    print()
    print("=================================")



#Done!!!!!