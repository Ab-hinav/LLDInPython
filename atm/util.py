
from enum import Enum

class Card:

    def __init__(self,card_number:int):
        self._card_number = card_number
        self._pin = 0

    def set_pin(self, pin:int):
        self._pin = pin

    def get_card_details(self):
        return self._card_number, self._pin
    

class BankingService:

    def __init__(self):
        self.__accounts ={}
        self.__card_pin_to_user_id = {}


    def load_data(self, card:Card,user_id:int):
        card_num,pin = card.get_card_details()
        self.__card_pin_to_user_id[str(card_num)+'_'+str(pin)] = user_id
        self.__accounts[user_id] = 1000

    def authenticate(self, card:Card):
        card_number, pin = card.get_card_details()
        if str(card_number)+'_'+str(pin) in self.__card_pin_to_user_id:
            return True, self.__card_pin_to_user_id[str(card_number)+'_'+str(pin)]
        
    def get_balance(self, user_id):
        return self.__accounts[user_id]

    def deduct_balance(self, user_id, amount):
        if amount > self.__accounts[user_id]:
            print('Insufficient balance')
            return False
        self.__accounts[user_id] -= amount

        print(f'Amount deducted: {amount} now balance ${self.__accounts[user_id]}')
        return True
    
    def add_balance(self, user_id, amount):
        self.__accounts[user_id] += amount
        print(f'Amount added: {amount} now balance ${self.__accounts[user_id]}')
        return True

        

class CashDispenser:

    def __init__(self):
       self.__cash_avaiable = 1000

    def load_cash(self, amount):
        self.__cash_avaiable += amount

    def dispense_cash(self, amount):
        if amount > self.__cash_avaiable:
            print('Not enough cash')
            return False
        else:
            self.__cash_avaiable -= amount
            print(f'Cash dispensed: {amount}')
            return True
        

class OPERATION_ALLOWED(Enum):
    CHECK_BALANCE = 1
    WITHDRAW = 2
    DEPOSIT = 3


