if __name__ == "__main__":
    account_num = int(input("Write account number: "))
    account_holder = input("Write account holder: ")
    account = PersonalAccount(account_num, account_holder)
    
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transaction History\n5. Exit")
        action = input("Choose an option: ")
        
        if action == '1':
            amount = float(input("Write deposit: "))
            account.deposit(amount)
        elif action == '2':
            amount = float(input("Write withdrawal: "))
            account.withdraw(amount)
        elif action == '3':
            print(f"Balance: ${account.get_balance():.2f}")
        elif action == '4':
            account.transaction_history()
        elif action == '5':
            break