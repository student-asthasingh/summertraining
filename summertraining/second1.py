import random

class BankAccount:
    used_account_numbers = set()

    def __init__(self, account_holder, initial_balance):
        self.account_number = self.generate_account_number()
        self.account_holder = account_holder
        self.balance = initial_balance

    def generate_account_number(self):
        while True:
            number = str(random.randint(10**15, 10**16 - 1))  # 16-digit number
            if number not in BankAccount.used_account_numbers:
                BankAccount.used_account_numbers.add(number)
                return number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance:.2f}")


class SavingAccount(BankAccount):
    INTEREST_RATE = 0.04  # 4%

    def __init__(self, account_holder, initial_balance):
        super().__init__(account_holder, initial_balance)

    def apply_interest(self):
        interest = self.balance * SavingAccount.INTEREST_RATE
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} added.")


class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 50000  # ₹50,000

    def __init__(self, account_holder, initial_balance):
        super().__init__(account_holder, initial_balance)

    def withdraw(self, amount):
        if amount <= self.balance + CurrentAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Withdrawal exceeds overdraft limit!")


def main():
    print("Welcome to Python Bank!")
    print("Select Account Type:")
    print("1. Saving Account")
    print("2. Current Account")
    choice = input("Enter choice (1 or 2): ")

    name = input("Enter account holder name: ")
    balance = float(input("Enter initial deposit amount: "))

    if choice == '1':
        account = SavingAccount(name, balance)
        print("\n--- Saving Account Created Successfully ---")
        account.display()
        account.apply_interest()
        account.display()

    elif choice == '2':
        account = CurrentAccount(name, balance)
        print("\n--- Current Account Created Successfully ---")
        account.display()

        withdraw_amount = float(input("Enter amount to withdraw: "))
        account.withdraw(withdraw_amount)
        account.display()

    else:
        print("Invalid choice. Exiting program.")


if __name__ == "__main__":
    main()
