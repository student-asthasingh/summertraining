import random

class BankAccount:
    interest_rate = 0.04  # 4% interest

    def __init__(self, acc_type, holder_name, balance):
        self.account_type = acc_type
        self.holder_name = holder_name
        self.balance = balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        return str(random.randint(10**15, 10**16 - 1))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance:.2f}")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest ₹{interest:.2f} applied at rate {self.interest_rate*100}%.")

# --- Program starts here ---

# Get account details
acc_type = input("Enter account type (saving/current): ").strip().lower()
holder_name = input("Enter account holder name: ").strip()
initial_balance = float(input("Enter initial balance: "))

# Create account
account = BankAccount(acc_type, holder_name, initial_balance)

# Display confirmation
print("\n      Your account has been created successfully.")
print(f"      Account Number: {account.account_number}")
print(f"      Interest Rate (Bank Fixed): {int(account.interest_rate * 100)}%\n")

# Main menu loop
while True:
    print("\nChoose operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Apply Interest (Bank-decided rate)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == '3':
        account.display_balance()

    elif choice == '4':
        account.apply_interest()

    elif choice == '5':
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 5.")
