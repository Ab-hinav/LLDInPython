from enum import Enum
import random 

from abc import ABC, abstractmethod


class CURRENCY(Enum):
    INR = 1
    USD = 2
    EUR = 3
    GBP = 4
    JPY = 5


class CurrencyConverter:


    _currency_convertion_table = {
        CURRENCY.INR: {
            CURRENCY.USD: 0.014,
            CURRENCY.EUR: 0.013,
            CURRENCY.GBP: 0.011,
            CURRENCY.JPY: 1.48
        },
        CURRENCY.USD: {
            CURRENCY.INR: 71.43,
            CURRENCY.EUR: 0.84,
            CURRENCY.GBP: 0.72,
            CURRENCY.JPY: 110.14
        },
        CURRENCY.EUR: {
            CURRENCY.INR: 78.85,
            CURRENCY.USD: 1.19,
            CURRENCY.GBP: 0.86,
            CURRENCY.JPY: 129.52
        },
        CURRENCY.GBP: {
            CURRENCY.INR: 90.34,
            CURRENCY.USD: 1.38,
            CURRENCY.EUR: 1.17,
            CURRENCY.JPY: 151.05
        },
        CURRENCY.JPY: {
            CURRENCY.INR: 0.67,
            CURRENCY.USD: 0.009,
            CURRENCY.EUR: 0.0077,
            CURRENCY.GBP: 0.0066
        }
    }

    @classmethod
    def convert(cls, from_currency, to_currency, amount):
        return amount * cls._currency_convertion_table[from_currency][to_currency]
        




class PaymentMethod(ABC):

    def __init__(self,method_name):
        self.method_name = method_name

    @abstractmethod
    def pay(self, amount,source_account,destination_account,currency):
        pass


class CreditCard(PaymentMethod):

    def __init__(self, method_name):
        super().__init__(method_name)

    def pay(self, amount, source_account, destination_account,currency):
        print('Creating transaction ....')
        transaction = Transaction(random.randint(1,999), amount, source_account, destination_account,self.method_name,currency)
        print('Deducting balance ....')
        source_account.deduct_balance(transaction)
        print('Adding balance ....')
        destination_account.add_balance(transaction)
        


class DebitCard(PaymentMethod):

    def __init__(self, method_name):
        super().__init__(method_name)

    def pay(self, amount, source_account, destination_account,currency):
        print('Creating transaction ....')
        transaction = Transaction(random.randint(1, 999), amount, source_account, destination_account,self.method_name,currency)
        print('Deducting balance ....')
        source_account.deduct_balance(transaction)
        print('Adding balance ....')
        destination_account.add_balance(transaction)
        


class Transaction:

    def __init__(self, transaction_id, amount, source_account, destination_account, payment_method , currency:CURRENCY):


        self.currency = currency
        self.transaction_id = transaction_id
        self.amount = amount
        self.source_account = source_account
        self.destination_account = destination_account
        self.payment_method = payment_method


class Account:

    def __init__(self, account_number, balance,currency:CURRENCY):
        self.currency = currency
        self.account_number = account_number
        self.balance = balance
        self.transactions = []


    def add_balance(self, transaction):
        if self.currency != transaction.currency:
            transaction.amount = CurrencyConverter().convert(transaction.currency, self.currency, transaction.amount)

        self.transactions.append(transaction)
        self.balance += transaction.amount

    def deduct_balance(self, transaction):

        if self.currency != transaction.currency:
            transaction.amount = CurrencyConverter().convert(transaction.currency, self.currency, transaction.amount)


        self.transactions.append(transaction)
        if self.balance < transaction.amount:
            raise Exception("Insufficient balance")
        self.balance -= transaction.amount

    


class User:

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name






class DigitalWallet:

    _instance = None

    @classmethod
    def get_instance(cls):
        if DigitalWallet._instance is None:
            DigitalWallet._instance = cls()
            return DigitalWallet._instance
        return DigitalWallet._instance


    def __init__(self):

        self.users = {}
        self.accounts = {}
        self.user_payment_methods = {}


    def add_user(self, user:User):
        self.users[user.user_id] = user

    def add_account(self, account:Account):
        self.accounts[account.account_number] = account

    def add_payment_method(self,user:User ,payment_method:PaymentMethod):
        if user.user_id not in self.user_payment_methods:
            self.user_payment_methods[user.user_id] = []
        if payment_method in self.user_payment_methods[user.user_id]:
            print('Payment method already exists')
            return
        current_user_payment_methods = self.user_payment_methods[user.user_id]
        current_user_payment_methods.append(payment_method)
        
        return current_user_payment_methods
    
    def get_user_payment_method(self, user:User):
        if user.user_id not in self.user_payment_methods:
            raise Exception("User not found")
        return self.user_payment_methods[user.user_id][0]
    
    def make_transaction(
        self,
        source_account: Account,
        destination_account: Account,
        amount,
        payment_method: PaymentMethod,
        currency: CURRENCY,
    ):
        payment_method.pay(amount, source_account, destination_account, currency)


    

class DigitalWalletDemo:

    @classmethod
    def run(cls):
        digital_wallet = DigitalWallet.get_instance()
        user1 = User(1, "Abhinav")
        user2 = User(2, "Rahul")
        digital_wallet.add_user(user1)
        digital_wallet.add_user(user2)

        account1 = Account(1, 1000, CURRENCY.INR)
        account2 = Account(2, 1000, CURRENCY.INR)
        digital_wallet.add_account(account1)
        digital_wallet.add_account(account2)

        payment_method1 = CreditCard("Credit Card")
        payment_method2 = DebitCard("Debit Card")

        digital_wallet.add_payment_method(user1, payment_method1)
        digital_wallet.add_payment_method(user2, payment_method2)

        digital_wallet.make_transaction(account1, account2, 100, payment_method1, CURRENCY.INR)
        digital_wallet.make_transaction(account2, account1, 100, payment_method2, CURRENCY.INR)

        print(account1.balance)
        print(account2.balance)
