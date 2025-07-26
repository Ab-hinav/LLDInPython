
from util import Inventory,CoffeType

class CoffeMachine:

    __instance = None
    __isInitialized = False

    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super(CoffeMachine,cls).__new__(cls)
        return cls.__instance
    


    def __init__(self,inventory:Inventory,coffeTypes:list[CoffeType]):

        if self.__isInitialized:
            return
        self.__isInitialized = True
        self.inventory = inventory
        self.coffeTypes = coffeTypes
        self.__selected_coffe = None

    def select_coffe(self,selectedOption:int):
        self.__selected_coffe = self.coffeTypes[selectedOption-1]
        print(f'Selected coffe is {self.__selected_coffe.get_name()}')
        return True

    def menu(self):
        optionNumber = 1
        print('Printing Menu------')
        for coffeType in self.coffeTypes:
            if self.inventory.can_make_recipe(coffeType.get_recipe()):
                print(f' ${optionNumber} {coffeType.get_name()} for only ${coffeType.get_price()}')
                optionNumber += 1

        if optionNumber <3:
            self.notifyIfInventoryLow()
            print('No coffe available')

        print('-------------')

    def make_payment(self,amount:int):
        if self.__selected_coffe.get_price() > amount:
            print('Not enough money')
            print(' Select another coffee')
            print('-------------')
            return False
        else:
            print('Payment successful')
            self.make_coffe()
            print(f'returning ${amount - self.__selected_coffe.get_price()} amount ')
            print('-------------')

    def make_coffe(self):
        if self.__selected_coffe is None:
            print('No coffe selected')
            return False
        else:
            if self.inventory.can_make_recipe(self.__selected_coffe.get_recipe()):
                self.inventory.deduct_recipe(self.__selected_coffe.get_recipe())
                print(f'Here is your {self.__selected_coffe.get_name()}')
                print('-------------')
                return True
            else:
                print('Not enough ingredients')
                print('-------------')
                return False
            
    def notifyIfInventoryLow(self):
        self.inventory.notify_if_low()
    