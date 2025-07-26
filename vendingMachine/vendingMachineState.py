from abc import ABC, abstractmethod
from typing import Optional


class VendingMachineState(ABC):
    
    
    @property
    def vending_machine_ctx(self):
        return self._vending_machine_ctx
    
    @vending_machine_ctx.setter
    def vending_machine_ctx(self,vending_machine):
        self._vending_machine_ctx = vending_machine
        
    
    @abstractmethod
    def select_product(self, tray_index: int, quantity: int):
        pass
    
    @abstractmethod
    def to_pay(self):
        pass
    
    @abstractmethod
    def insert_money(self):
        pass
    
    
    @abstractmethod
    def cancel_transaction(self):
        pass
    
    @abstractmethod
    def return_change(self):
        pass
    
    @abstractmethod
    def restock_inventory(self, tray_index: int, product, quantity: int):
        pass
    
    @abstractmethod
    def restock_money(self, money_type: Optional[str] = None, denom: Optional[str] = None, quantity: Optional[int] = None):
        pass