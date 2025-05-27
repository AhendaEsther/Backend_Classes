class Account:
    def __init__(self,name):
        self.name=name
        self.balance=0
        self.deposit=[]
        self.withdrawals=[]
        self.transaction=[]
        self.loan=[]
        self.minimal_balance=0


# Deposit: method to deposit funds, store the deposit and return a message with the new balance to the customer. It should only accept positive amounts.
    def deposits(self,amount):
        if amount >=0:
            self.deposit.append(amount)
            self.balance += amount
            return f"Hello {self.name}, you have received {amount}. Your new balance is {self.balance}"
        else:
            return f"invalid deposit amount"

# Withdraw: method to withdraw funds, store the withdrawal and return a message with the new balance to the customer. An account cannot be overdrawn.
    def withdraw(self,amount):
        if amount<=0:
            return f"{self.name} your account have negative value"
        else:
            self.balance -= amount
            self.withdrawals.append(amount)
            return f"Hello {self.name} you have withdrawn {amount} your new balance is {self.balance}"

# Transfer Funds: Method to transfer funds from one account to an instance of another account.
    def transfer(self, amount):
        self.balance -= amount
        self.transaction.append(amount)
        return f"You have transfered {amount} and your new balance is {self.balance}"

# Get Balance: Method to calculate an account balance from deposits and withdrawals.
    def get_balance(self):
        return f"{self.name} your new balance is {self.balance} "


# Request Loan: Method to request a loan amount.
    def request_loan(self,amount):
        if amount>0:
            self.loan.append(amount)
            self.loan = amount
            return f"Your not eligible for a loan"
        else:
             return f"your loan has been approved"


# Repay Loan: Method to repay a loan with a given amount.
     def repay_loan(self,amount):
         if amount>self.loan:
            self.loan.append(amount)
             self.loan +=amount
             return "your loan has been paid"
         else:
            return f"Your loan has not been fully paid"




# View Account Details: Method to display the account owner's details and current balance.

    def view_details(self):
        return f"Hello {self.name}you account balance is {self.balance} and you withdrawed {self.withdrawal}. you had a loan of {self.loan} and you repayed {self.loan}."

# Change Account Owner: Method to update the account owner's name.

    def change_owner(self,new_name):
        self.name = new_name
        return f"your name is {new_name}"

    # Account Statement: Method to generate a statement of all transactions in an account. (Print using a for loop).
    def account_statement(self):
        for i in self.transactions:
            return f"{self.transactions}"
    

# Interest Calculation: Method to calculate and apply an interest to the balance. Use 5% interest. 

    def interest_calculation(self,time):
        self.balance=self.balance*0.5*time
        return f"Your intrest is {self.balance}"

# Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons.
    def freeze_account(self,freeze):
        if freeze == "true":
            return f"your account is freezed"
        else:
            return f"is unfreezed"

# Set Minimum Balance: Method to enforce a minimum balance requirement. You cannot withdraw if your balance is less than this amount.Close Account: Method to close the account and set all balances to zero and empty all transactions.

    def minimum_balance(self, amount):
        min_balance = 100
        if self.balance - amount >= min_balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return f"Withdrawal denied. Minimum balance of ${min_balance} must be maintained."
    def close_account(self):
        self.deposits=[]
        self.withdrawal=[]
        self.transactions=[]
        self.balance=0
        self.loan=0
        return f"{self.name} your account is closed"