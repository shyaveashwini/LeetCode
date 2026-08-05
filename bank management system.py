class Account:
    def __init__(self,bank_account,holder_name,balance):
        self.bank_account=bank_account
        self.holder_name=holder_name
        self.balance=balance

    def display(self):
        print("Bank_account:",self.bank_account,"\nHolder_name=",self.holder_name,"\nBalance=",self.balance)

    def deposit(self,amount):
        self.balance+=amount
        print("amount deposited successfully.")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print("amount withdrawn successfully")
        else:
            print("not sufficient balance")


    def get_balance(self):
        return self.balance

class SavingsAccount(Account):

    def __init__(self, account_no, holder_name, balance, interest_rate):
        super().__init__(account_no, holder_name, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Savings Account: Insufficient balance.")

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Interest added:", interest)

class CurrentAccount(Account):

    def __init__(self, account_no, holder_name, balance, overdraft_limit):
        super().__init__(account_no, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Overdraft limit exceeded.")

class Bank:

    def __init__(self):
        self.accounts = []

    def create_account(self, account):
        self.accounts.append(account)
        print("Account created successfully.")

    def search_account(self, account_no):
        for account in self.accounts:
            if account.account_no == account_no:
                return account
        return None

    def deposit(self, account_no, amount):
        account = self.search_account(account_no)

        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_no, amount):
        account = self.search_account(account_no)

        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transfer(self, sender_no, receiver_no, amount):

        sender = self.search_account(sender_no)
        receiver = self.search_account(receiver_no)

        if sender is None:
            print("Sender account not found.")
            return

        if receiver is None:
            print("Receiver account not found.")
            return

        if sender.get_balance() >= amount:

            sender.withdraw(amount)
            receiver.deposit(amount)

            print("Transfer successful.")

        else:
            print("Insufficient balance.")

    def display_accounts(self):

        if len(self.accounts) == 0:
            print("No accounts found.")
        else:
            for account in self.accounts:
                account.display()
                print("-" * 30)


bank = Bank()

while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. Display Accounts")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        account_no = int(input("Enter Account Number: "))
        name = input("Enter Holder Name: ")
        balance = float(input("Enter Initial Balance: "))
        interest = float(input("Enter Interest Rate: "))

        account = SavingsAccount(account_no, name, balance, interest)

        bank.create_account(account)

    elif choice == 2:

        account_no = int(input("Enter Account Number: "))
        name = input("Enter Holder Name: ")
        balance = float(input("Enter Initial Balance: "))
        overdraft = float(input("Enter Overdraft Limit: "))

        account = CurrentAccount(account_no, name, balance, overdraft)

        bank.create_account(account)

    elif choice == 3:

        account_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount: "))

        bank.deposit(account_no, amount)

    elif choice == 4:

        account_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount: "))

        bank.withdraw(account_no, amount)

    elif choice == 5:

        sender = int(input("Enter Sender Account Number: "))
        receiver = int(input("Enter Receiver Account Number: "))
        amount = float(input("Enter Amount: "))

        bank.transfer(sender, receiver, amount)

    elif choice == 6:

        bank.display_accounts()

    elif choice == 7:

        print("Thank you!")
        break

    else:
        print("Invalid choice.")

