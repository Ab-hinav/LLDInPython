from vendingMachine import VendingMachine
from product import Product
    




if __name__ == '__main__':
    print("Hello World")
    
    vendingMachine_instance = VendingMachine(3,10)
    vendingMachine_instance.state.restock_inventory(0,Product("toffee",10),10)
    vendingMachine_instance.state.restock_inventory(1,Product("chips",15),10)
    vendingMachine_instance.state.restock_inventory(2,Product("chocolate",30),10)
    
    vendingMachine_instance.state.restock_money()
    
    # select product
    vendingMachine_instance.select_product(0,1)
    vendingMachine_instance.state.to_pay()
    vendingMachine_instance.state.insert_money()
    vendingMachine_instance.state.dispense_product()
    vendingMachine_instance.state.return_change()
    
    
