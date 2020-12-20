# SENIH UCAR
import re

class BankAccount:#BankAccount

    def __init__(self,name,balance):
        """
        constructor that takes two parameters name and balance.
        :param name: account name
        :param balance: account balance
        """
        if str.isspace(name) == True:
            raise ValueError("Name cannot be empty")
        if bool(re.search("^[a-zA-Z]([\w -]*[a-zA-Z])?$", name)) == False:
            raise ValueError("Name cannot include numbers or symbols")
        else:
            self.name = name.title()
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        if balance >= 0:
            self.balance = float("%.2f" % balance)

    def displayDetails(self):
        """
        The method will display the name and the balance in an organized manner
        """
        print(" Account name is :",self.name)
        print(" Account balance is :", self.balance)

    def methodDeposit(self,deposit_amount):
        """
        the method accepts amount as a parameter. If the passed parameter was positive it will be added to the
        balance otherwise, a Value Error will be raised with the message “amount cannot be zero or less”
        :param deposit_amount: deposit amount
        :return:
        """
        if deposit_amount > 0:
            balance = self.balance + float(deposit_amount)
            self.balance = float("%.2f" % balance)
        else:
            raise ValueError("Amount cannot be zero or less")

    def methodWithdraw(self,withdraw_amount):
        """
        o	If the passed parameter was negative or zero a Value Error will be raised (“ amount cannot be zero or less than zero”
        o	If the passed parameter was greater than balance a Value Error will be raised “Insufficient funds”
        o	If the amount was valid i.e. greater than 0 and less or equal to the balance, the amount will be deducted from the balance
        :param withdraw_amount: withdraw amount
        :return:
        """
        if withdraw_amount <= 0 :
            raise ValueError("Amount cannot be zero or less than zero")
        if withdraw_amount > self.balance:
            raise ValueError("Insufficient funds")
        if withdraw_amount > 0 and withdraw_amount == self.balance or withdraw_amount < self.balance :
            balance = self.balance - withdraw_amount
            self.balance = float("%.2f" % balance)
