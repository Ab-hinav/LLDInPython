from enum import Enum


class COFFE(Enum):
    ESPRESSO = "EXPRESSO"
    LATTE = "Latte"
    CAPPUCCINO = "Cappucino"


class Item(Enum):
    ARABICA = "arabica"
    ROBUSTA = "robusta"
    LUNGO = "lungo"
    MILK = "milk"
    SUGAR = "sugar"
    CARAMEL = "caramel"


class Recipe:
    def __init__(self):
        self.__recipe = {}

    def add_item(self, item: Item, quantity: int):
        self.__recipe[item] = quantity

    def get_recipe(self):
        return self.__recipe


class Inventory:
    def __init__(self):
        self.__inventory = {}

    def add_item(self, item: Item, quantity: int):
        self.__inventory[item] = quantity

    def get_inventory(self):
        return self.__inventory

    def can_make_recipe(self, recipe:Recipe):
        for item, quantity in recipe.get_recipe().items():
            if item not in self.__inventory or self.__inventory[item] < quantity:
                return False
        return True
    
    def deduct_recipe(self, recipe:Recipe):
        for item, quantity in recipe.get_recipe().items():
            self.__inventory[item] -= quantity

    def notify_if_low(self):
        for item, quantity in self.__inventory.items():
            if quantity < 5:
                print(f'Low on {item.value}')
                print(f'Please restock {item.value}')
                print('-----------------')


class CoffeType:
    def __init__(self, coffe: COFFE, price, recipe: Recipe):
        self.__coffe = coffe
        self.__price = price
        self.__recipe = recipe

    def get_name(self):
        return self.__coffe._value_


    def get_recipe(self):
        return self.__recipe
    
    def get_price(self):
        return self.__price
    
    def get_coffe(self):
        return self.__coffe

