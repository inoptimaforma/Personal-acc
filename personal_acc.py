class PersonalAccount:
    def __init__(self, account_num: int, account_holder: str):
        self.account_num = account_num
        self.account_holder = account_holder
        self.__balance = 0.0
        self.transactions = []

    def deposit(self, amount: float):
        transaction = Amount(amount, 'DEPOSIT')
        self.transactions.append(transaction)
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount > self.__balance:
            print("Not enough money")
            return
        transaction = Amount(amount, 'WITHDRAWAL')
        self.transactions.append(transaction)
        self.__balance -= amount

    def transaction_history(self):
        for transaction in self.transactions:
            print(transaction)
    def get_balance(self):
        return self.__balance
    def get_account_num(self):
        return self.account_num
    def set_account_num(self, account_num: int):
        self.account_num = account_num
    def get_account_holder(self):
        return self.account_holder
    def set_account_holder(self, account_holder: str):
        self.account_holder = account_holder
    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: ${self.__balance:.2f}"
    def __add__(self, amount: float):
        self.deposit(amount)
        return self
    def __sub__(self, amount: float):
        self.withdraw(amount)
        return self
