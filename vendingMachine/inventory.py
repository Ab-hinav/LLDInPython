from product import Product

class Tray:
    def __init__(self,num_of_product:int):
        self.products:list[Product] = []
        self.num_of_product = num_of_product
        
    def add_product(self,product:Product):
        self.products.append(product)

    def remove_product(self):
        return self.products.pop()
        
    def get_product(self):
        return self.products[-1]
    
    def get_num_of_product(self):
        return self.num_of_product
    
    


class Inventory:
    
    def __init__(self,num_of_tray:int,tray_size:int):
        self.inventory = {}
        for i in range(num_of_tray):
            self.inventory[i] = Tray(tray_size)
            
    def add_product(self,tray_index:int,product:Product,quantity:int):
        for i in range(quantity):
            self.inventory[tray_index].add_product(product)
        
    def remove_product(self,tray_index:int,quantity:int):
        for i in range(quantity):
            self.inventory[tray_index].remove_product()
        
    def get_product(self,tray_index:int):
        return self.inventory[tray_index].get_product()
    
    def get_num_of_product(self,tray_index:int):
        return self.inventory[tray_index].get_num_of_product()
    
    
    
    