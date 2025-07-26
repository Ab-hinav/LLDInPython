from vendingMachineState import VendingMachineState
from product import Coin, Notes
from util import Money


class IdleState(VendingMachineState):

    def select_product(self,tray_index:int,quantity:int):
        if self.vending_machine_ctx.inventory.get_num_of_product(tray_index) < quantity:
            print("Not enough product in the tray")
            return
        self.vending_machine_ctx._selected_tray_index = tray_index
        self.vending_machine_ctx._selected_quantity = quantity
        print(f"Selected {quantity} products from tray {tray_index}")
       
    def insert_money(self,money):
        print("Not allowed to insert money in idle state")
        
    def cancel_transaction(self):
        print("Not allowed to cancel transaction in idle state")
        
    def return_change(self):
        print("Not allowed to return change in idle state")
        
        
        
    def __init__(self):
        print("IdleState initialized")
        
        
    def restock_inventory(self,tray_index:int,product,quantity:int):
        self.vending_machine_ctx.inventory.add_product(tray_index,product,quantity)
        
    
    def __restock_note(self):
        note = int(input("""Enter the note you want to restock: from the following list of notes
                     1 FIFTY
                     2 HUNDRED
                     3 TWO_HUNDRED
                     4 FIVE_HUNDRED
                     5 TWO_THOUSAND
                     """))
        quantity = int(input("Enter the quantity you want to restock: "))
        
        match note:
            case 1:
                self.vending_machine_ctx.money.add_note(Notes.FIFTY,quantity)
            case 2:
                self.vending_machine_ctx.money.add_note(Notes.HUNDRED,quantity)
            case 3:
                self.vending_machine_ctx.money.add_note(Notes.TWO_HUNDRED,quantity)
            case 4:
                self.vending_machine_ctx.money.add_note(Notes.FIVE_HUNDRED,quantity)
            case 5:
                self.vending_machine_ctx.money.add_note(Notes.TWO_THOUSAND,quantity)
            case _:
                print('invalid note')
                
        

    
    def __restock_coin(self):
        coin = int(input("""Enter the coin you want to restock: 
                         1 ONE
                         2 TWO
                         3 FIVE
                         4 TEN
                         5 TWENTY
                         """))
        quantity = int(input("Enter the quantity you want to restock: "))
        
        match coin:
            case 1:
                self.vending_machine_ctx.money.add_coin(Coin.ONE,quantity)
            case 2:
                self.vending_machine_ctx.money.add_coin(Coin.TWO,quantity)
            case 3:
                self.vending_machine_ctx.money.add_coin(Coin.FIVE,quantity)
            case 4:
                self.vending_machine_ctx.money.add_coin(Coin.TEN,quantity)
            case 5:
                self.vending_machine_ctx.money.add_coin(Coin.TWENTY,quantity)
            case _:
                print('invalid coin')
                
                
    
    
    def restock_money(self):
        
        print("Restocking money")
        while True:
            resp = input("Enter the note or coin you want to restock (type 'done' to finish): ")
        
            if resp == "note":
                self.__restock_note()
            elif resp == "coin":
                self.__restock_coin()
            elif resp == "done":
                break
            else:
                print("Invalid input")
                
        print("Money restocked successfully")
        
    
    
    def to_pay(self):
        print("To pay")
        amount = self.vending_machine_ctx.inventory.get_product(self.vending_machine_ctx._selected_tray_index).price * self.vending_machine_ctx._selected_quantity
        print(f"Amount to pay: {amount}")
        self.vending_machine_ctx.transition_state(ReadyState())
        
    def dispense_product(self):
        print("Cannot dispense product in idle state")
        
    
        
        
    
        
    
    
class ReadyState(VendingMachineState):
    
    def __init__(self):
        print("ReadyState initialized")
        
        
    def to_pay(self):
        pass
    
    def insert_money(self):
        
        print("Insert money")
        money_inserted = Money()
        while True:
            
            type = input("Enter the coin/note you want to insert: type done to finish ")
            if type == "done":
                break
            if type == "coin":
                coin = int(input("""Enter the coin  you want to insert:
                             1 ONE
                             2 TWO
                             3 FIVE
                             4 TEN
                             5 TWENTY
                             """))
                qty = int(input("Enter the quantity you want to insert: "))
                match coin:
                    case 1:
                        money_inserted.add_coin(Coin.ONE,qty)
                    case 2:
                        money_inserted.add_coin(Coin.TWO,qty)
                    case 3:
                        money_inserted.add_coin(Coin.FIVE,qty)
                    case 4:
                        money_inserted.add_coin(Coin.TEN,qty)
                    case 5:
                        money_inserted.add_coin(Coin.TWENTY,qty)
                    case _:
                        print("Invalid coin")
                
            elif type == "note":
                note = int(input("""Enter the note  you want to insert:
                             1 FIFTY
                             2 HUNDRED
                             3 TWO_HUNDRED
                             4 FIVE_HUNDRED
                             5 TWO_THOUSAND
                             """))
                qty = int(input("Enter the quantity you want to insert: "))
                match note:
                    case 1:
                        money_inserted.add_note(Notes.FIFTY,qty)
                    case 2:
                        money_inserted.add_note(Notes.HUNDRED,qty)
                    case 3:
                        money_inserted.add_note(Notes.TWO_HUNDRED,qty)
                    case 4:
                        money_inserted.add_note(Notes.FIVE_HUNDRED,qty)
                    case 5:
                        money_inserted.add_note(Notes.TWO_THOUSAND,qty)
                    case _:
                        print("Invalid note")
                        
        money_to_pay = self.vending_machine_ctx.inventory.get_product(self.vending_machine_ctx._selected_tray_index).price * self.vending_machine_ctx._selected_quantity
        
        print(f"Money to pay: {money_to_pay}")
        print(f"Money inserted: {money_inserted.get_total_amount()}")
        
        if money_inserted.get_total_amount() < money_to_pay:
            print("Not enough money inserted")
            print("Returning money")
            self.vending_machine_ctx.transition_state(IdleState())
        else:
            print("Processing transaction")
            self.vending_machine_ctx.inserted_money = money_inserted
            self.vending_machine_ctx.transition_state(DispenceState())
        
        
    def cancel_transaction(self):
        print("Cannot cancel transaction in ready state")
        
    def return_change(self):
        print("Cannot return change in ready state")
        
    def restock_inventory(self,tray_index:int,product,quantity:int):
        print("Cannot restock inventory in ready state")
        
    def restock_money(self):
        print("Cannot restock money in ready state")
        
    def select_product(self,tray_index:int,quantity:int):
        print("Cannot select product in ready state")
        
    def dispense_product(self):
        print("Cannot dispense product in ready state")
        
        
        
        
class DispenceState(VendingMachineState):
    
    def __init__(self):
        print("DispenceState initialized")
        
                
        
        
        
    def dispense_product(self):
        print("Dispensing product")
        # check if change is enough        
        self.vending_machine_ctx.inventory.remove_product(self.vending_machine_ctx._selected_tray_index,self.vending_machine_ctx._selected_quantity)
        print(f"Dispensed {self.vending_machine_ctx._selected_quantity} products from tray {self.vending_machine_ctx._selected_tray_index}")
        
        
    def to_pay(self):
        print("Cannot to pay in dispense state")
        
    def insert_money(self):
        print("Cannot insert money in dispense state")
        
    def cancel_transaction(self):
        print("Cancelling transaction")
        print("Paying back the money")
        money_to_return = self._vending_machine_ctx.inserted_money
        print(f"Returning {money_to_return.get_total_amount()} money")
        self._vending_machine_ctx.inserted_money = Money()
        self._vending_machine_ctx.transition_state(IdleState())
        
        
    def return_change(self):
        print("Returning change")
        amount_to_return = self.vending_machine_ctx.inserted_money.get_total_amount() - self.vending_machine_ctx.inventory.get_product(self.vending_machine_ctx._selected_tray_index).price * self.vending_machine_ctx._selected_quantity
        print(f"Amount to return: {amount_to_return}")
        self.vending_machine_ctx.money.add_money(self.vending_machine_ctx.inserted_money)
        return amount_to_return
        
        
        
        
        
        
    def restock_inventory(self,tray_index:int,product,quantity:int):
        print("Cannot restock inventory in dispense state")
        
    def restock_money(self):
        print("Cannot restock money in dispense state")
        
    def select_product(self,tray_index:int,quantity:int):
        print("Cannot select product in dispense state")
        
    
        
        
        
        
        
             
        
            
        
        
        
        
            
        
        
        
    
    