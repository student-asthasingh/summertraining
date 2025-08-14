import random

class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        return str(random.randint(10**15, 10**16 - 1))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount:.2f} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance:.2f}")


class SavingAccount(BankAccount):
    interest_rate = 0.04  # 4%

    def apply_interest(self):
        interest = self.balance * SavingAccount.interest_rate
        self.balance += interest
        print(f"Interest ₹{interest:.2f} applied at {SavingAccount.interest_rate * 100:.0f}% rate.")


class CurrentAccount(BankAccount):
    overdraft_limit = 2000 

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif self.balance - amount >= -CurrentAccount.overdraft_limit:
            self.balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")
        else:
            print("Overdraft limit exceeded. Transaction denied.")

acc_type = input("Enter account type (saving/current): ").strip().lower()
holder_name = input("Enter account holder name: ").strip()
initial_balance = float(input("Enter initial balance: "))

if acc_type == "saving":
    account = SavingAccount(holder_name, initial_balance)
    print("\n      Your Saving Account has been created successfully.")
    print(f"      Account Number: {account.account_number}")
    print(f"      Interest Rate (Bank Fixed): {SavingAccount.interest_rate * 100:.0f}%")
elif acc_type == "current":
    account = CurrentAccount(holder_name, initial_balance)
    print("\n      Your Current Account has been created successfully.")
    print(f"      Account Number: {account.account_number}")
    print(f"      Overdraft Limit (Bank Fixed): ₹{CurrentAccount.overdraft_limit}")
else:
    print("Invalid account type. Please restart and choose 'saving' or 'current'.")
    exit()

while True:
    print("\nChoose operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    if isinstance(account, SavingAccount):
        print("4. Apply Interest")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == '3':
        account.display_balance()

    elif choice == '4' and isinstance(account, SavingAccount):
        account.apply_interest()

    elif choice == '5':
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice. Please try again.")
