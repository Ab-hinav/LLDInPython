from product import Notes, Coin

class Money:
    
    def __init__(self):
        self.notes = {
            Notes.TWO_THOUSAND: 0,
            Notes.FIVE_HUNDRED: 0,
            Notes.HUNDRED: 0,
            Notes.FIFTY: 0,
            Notes.TWENTY: 0,
            Notes.TEN: 0,
        }
        
        self.coins = {
            Coin.TWENTY: 0,
            Coin.TEN: 0,
            Coin.FIVE: 0,
            Coin.TWO: 0,
            Coin.ONE: 0,
        }
     
    
    def add_money(self,money):
        for note in money.notes.keys():
            self.notes[note] += money.notes[note]
            
        for coin in money.coins.keys():
            self.coins[coin] += money.coins[coin]
            
       
    def add_note(self,note:Notes,quantity:int):
        self.notes[note] += quantity
        
    def add_coin(self,coin:Coin,quantity:int):
        self.coins[coin] += quantity
        
    def remove_note(self,note:Notes,quantity:int):
        self.notes[note] -= quantity
        
    def remove_coin(self,coin:Coin,quantity:int):
        self.coins[coin] -= quantity
    
    def get_total_amount(self):
        amount =0
        for note in self.notes.keys():
            amount += note.value * self.notes[note]
        for coin in self.coins.keys():
            amount += coin.value * self.coins[coin]
        return amount
    
    def can_get_change(self,amount:int):
        noteCpy = self.notes.copy()
        coinCpy = self.coins.copy()
        
        for note in noteCpy.keys():
            while amount >= note.value and noteCpy[note] > 0:
                amount -= note.value
                noteCpy[note] -= 1
                
        for coin in coinCpy.keys():
            while amount >= coin.value and coinCpy[coin] > 0:
                amount -= coin.value
                coinCpy[coin] -= 1
                
        return amount == 0
    
    def get_change(self,money):
        change = Money()
        if self.can_get_change(money.get_total_amount()):
            pass
            for note in self.notes.keys():
                while money.notes[note] > 0 and self.notes[note] > 0:
                    money.notes[note] -= 1
                    self.notes[note] -= 1
                    change.notes[note] += 1
                    
            for coin in self.coins.keys():
                while money.coins[coin] > 0 and self.coins[coin] > 0:
                    money.coins[coin] -= 1
                    self.coins[coin] -= 1
                    change.coins[coin] += 1
            
        else:
            raise ValueError("Cannot get change")
        
        if money.get_total_amount() > 0:
            raise ValueError("Cannot get change idk why")
            
        return change
            
            
            