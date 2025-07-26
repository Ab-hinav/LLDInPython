from util import Recipe,COFFE,CoffeType,Inventory,Item
from coffeMachine import CoffeMachine


class CoffeMachineDemo:

    @classmethod
    def run(self):

        self.recipeForExpresso = Recipe()
        self.recipeForExpresso.add_item(Item.ARABICA,2)
        self.recipeForExpresso.add_item(Item.MILK, 1)

        self.recipeForLatter = Recipe()
        self.recipeForLatter.add_item(Item.CARAMEL, 1)
        self.recipeForLatter.add_item(Item.ROBUSTA, 2)
        self.recipeForLatter.add_item(Item.MILK, 3)

        self.recipeForCappucino = Recipe()
        self.recipeForCappucino.add_item(Item.LUNGO, 1)
        self.recipeForCappucino.add_item(Item.MILK, 2)
        self.recipeForCappucino.add_item(Item.SUGAR,1)
        self.recipeForCappucino.add_item(Item.CARAMEL, 4)

        self.expressoCoffe = CoffeType(COFFE.ESPRESSO,12,self.recipeForExpresso)
        self.latterCoffe = CoffeType(COFFE.LATTE, 15, self.recipeForLatter)
        self.cappucino = CoffeType(COFFE.CAPPUCCINO, 20, self.recipeForCappucino)

        self.inventory = Inventory()
        self.inventory.add_item(Item.ARABICA, 10)
        self.inventory.add_item(Item.ROBUSTA, 10)
        self.inventory.add_item(Item.CARAMEL, 10)
        self.inventory.add_item(Item.LUNGO, 10)
        self.inventory.add_item(Item.MILK, 10)
        self.inventory.add_item(Item.SUGAR, 5)

        self.coffeMachine = CoffeMachine( self.inventory,[self.expressoCoffe, self.latterCoffe, self.cappucino])

        while True:
            self.coffeMachine.menu()
            self.selectedOption = int(input('Select Coffe Type: type 0 to exit '))
            if self.selectedOption == 0:
                break
            self.add_money = int(input('Enter money: '))
            self.coffeMachine.select_coffe(self.selectedOption)
            self.coffeMachine.make_payment(self.add_money)



if __name__ == '__main__':
    CoffeMachineDemo.run()

