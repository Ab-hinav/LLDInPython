
from atmController import AtmController
from util import Card,OPERATION_ALLOWED







if __name__ == '__main__':

    atm = AtmController()

    card1 = Card(3452)
    card1.set_pin(123)

    card2 = Card(3245)
    card2.set_pin(123)

    atm.load_data(card1,222)
    atm.load_data(card2, 100)

    atm.show_current_state()
    atm.insert_card(card1)
    atm.enter_pin(123)
    atm.show_current_state()
    atm.select_operation(OPERATION_ALLOWED.CHECK_BALANCE)
    atm.show_current_state()




