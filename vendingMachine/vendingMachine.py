from inventory import Inventory
from util import Money
from vendingMachineState import VendingMachineState
from states import IdleState

# this must be a singleton

class VendingMachine:
    
    
    _instance = None
    _initialized = False
    
    def __new__(cls,*args, **kwargs):
        if cls._instance is None:
            cls._instance = super(VendingMachine,cls).__new__(cls)
        return cls._instance
    
    
    def __init__(self,num_of_tray:int,tray_size:int):
        if self._initialized:
            return 
        self.inventory = Inventory(num_of_tray,tray_size)
        self.money = Money()
        self.state = IdleState()
        self.inserted_money = Money()
        self._selected_tray_index = -1
        self._selected_quantity = -1
        self._initialized = True
        self.state.vending_machine_ctx = self
        
        
    def select_product(self,tray_index:int,quantity:int):
        self.state.select_product(tray_index,quantity)
    
    
    def restock_inventory(self,tray_index:int,product,quantity:int):
        self.state.restock_inventory(tray_index,product,quantity)
        
    def restock_money(self):
        self.state.restock_money()
        
    def insert_money(self):
        self.state.insert_money()
        
    def to_pay(self):
        self.state.to_pay()
        
    def cancel_transaction(self):
        self.state.cancel_transaction()
        
    def return_change(self):
        self.state.return_change()
        
    
    
    def transition_state(self,state:VendingMachineState):
        self.state = state
        state.vending_machine_ctx = self
        
    