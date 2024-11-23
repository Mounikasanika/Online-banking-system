class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f'Deposited: ${amount:.2f}')
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f'Withdrew: ${amount:.2f}')
            return True
        return False

    def transfer(self, amount, recipient):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            self.transactions.append(f'Transferred: ${amount:.2f} to {recipient.username}')
            return True
        return False

    def view_statement(self):
        print(f'Account Statement for {self.username}:')
        for transaction in self.transactions:
            print(transaction)
        print(f'Current Balance: ${self.balance:.2f}')


class Bank:
    def __init__(self):
        self.users = {}

    def create_account(self, username, password):
        if username not in self.users:
            self.users[username] = User(username, password)
            print(f'Account created for {username}.')
            return True
        print('Username already exists.')
        return False

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        print('Invalid username or password.')
        return None


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Online Banking System")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            bank.create_account(username, password)

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = bank.login(username, password)

            if user:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. View Statement")
                    print("5. Logout")
                    action = input("Choose an action: ")

                    if action == '1':
                        amount = float(input("Enter amount to deposit: "))
                        if user.deposit(amount):
                            print(f'Successfully deposited ${amount:.2f}.')
                        else:
                            print('Deposit failed. Please enter a valid amount.')

                    elif action == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        if user.withdraw(amount):
                            print(f'Successfully withdrew ${amount:.2f}.')
                        else:
                            print('Withdrawal failed. Please enter a valid amount.')

                    elif action == '3':
                        recipient_username = input("Enter recipient username: ")
                        recipient = bank.users.get(recipient_username)
                        if recipient:
                            amount = float(input("Enter amount to transfer: "))
                            if user.transfer(amount, recipient):
                                print(f'Successfully transferred ${amount:.2f} to {recipient_username}.')
                            else:
                                print('Transfer failed. Please enter a valid amount.')
                        else:
                            print('Recipient not found.')

                    elif action == '4':
                        user.view_statement()

                    elif action == '5':
                        print('Logging out...')
                        break

                    else:
                        print('Invalid action.')

        elif choice == '3':
            print('Exiting...')
            break

        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()