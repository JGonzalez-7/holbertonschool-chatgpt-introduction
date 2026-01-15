class Checkbook:
    # Function description:
    #   Track a simple account balance with deposit/withdraw actions.
    # Parameters:
    #   balance (float): Starts at 0.0 by default.
    # Returns:
    #   None
    def __init__(self):
        self.balance = 0.0

    # Function description:
    #   Add funds to the current balance.
    # Parameters:
    #   amount (float): Amount to deposit (non-negative expected).
    # Returns:
    #   None
    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    # Function description:
    #   Remove funds from the balance if sufficient.
    # Parameters:
    #   amount (float): Amount to withdraw (non-negative expected).
    # Returns:
    #   None
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    # Function description:
    #   Display the current balance.
    # Parameters:
    #   None
    # Returns:
    #   None
    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


# Function description:
#   Safely prompt the user for a numeric amount and handle bad input.
# Parameters:
#   prompt (str): Text to display to the user.
# Returns:
#   float | None: Parsed amount or None if input was invalid.
def prompt_amount(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return None


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = prompt_amount("Enter the amount to deposit: $")
            if amount is not None:
                cb.deposit(amount)
        elif action == 'withdraw':
            amount = prompt_amount("Enter the amount to withdraw: $")
            if amount is not None:
                cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
