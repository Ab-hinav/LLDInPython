

from util import OPERATION_ALLOWED,CashDispenser,BankingService


class AtmState():

    def insert_card(self,card:int):
        pass

    def enter_pin(self, pin:int):
        pass

    def load_data(self, card, user_id):
        pass

    def select_operation(self, operation:OPERATION_ALLOWED):
        pass


    @property
    def context(self):
        return self.__context
    
    @context.setter
    def context(self, context):
        self.__context = context


class IdleState(AtmState):

    def insert_card(self, card:int):
        self.context.__card = card

    def load_data(self,card,user_id):
        self.context._banking_service.load_data(card, user_id)

    def enter_pin(self, pin:int):
        self.context.__card.set_pin(pin)
        isAuth,self.context._curr_user_id = self.context._banking_service.authenticate(self.context.__card)

        if isAuth:
            self.context.change_state(AuthenticatedState())
        else:
            print('Invalid Pin')
        print('removing card')
        self.context.__card = None

    def select_operation(self, operation:OPERATION_ALLOWED):
        raise Exception("Invalid Operation")


class AuthenticatedState(AtmState):

    def insert_card(self, card:int):
        raise Exception("Invalid Operation")
    
    def load_data(self,card,user_id):
        raise Exception("Invalid operation")

    def enter_pin(self, pin:int):
       raise Exception("Invalid Operation")

    def select_operation(self, operation:OPERATION_ALLOWED):


        match(operation):
            case OPERATION_ALLOWED.CHECK_BALANCE:
                
                res = self.context._banking_service.get_balance(self.context._curr_user_id)
                print(f'Balance is {res}')
                self.context._curr_user_id = -1
                self.context.change_state(IdleState())

            case OPERATION_ALLOWED.DEPOSIT:

                res = self.context._banking_service.add_balance(self.context._curr_user_id, 100)
                self.context._curr_user_id = -1
                self.context.change_state(IdleState())
                

            case OPERATION_ALLOWED.WITHDRAW:

                res = self.context._banking_service.deduct_balance(self.context._curr_user_id, 100)
                self.context._curr_user_id = -1
                self.context.change_state(IdleState())
            
            case _:
                raise Exception("Invalid Operation")
    


class AtmController:

    __instance = None
    __isInit = False

    def __new__(cls):

        if cls.__instance is None:
            cls.__instance = super(AtmController,cls).__new__(cls)
        return cls.__instance
    
    def __init__(self):

        if self.__isInit:
            return
        self.__isInit = True
        self.__card = None
        self.__cash_dispensor = CashDispenser()
        self._banking_service = BankingService()
        self._curr_user_id = -1
        self.__current_state = IdleState()
        self.__current_state.context = self


    def change_state(self, state:AtmState):
        self.__current_state = state
        self.__current_state.context = self

    def insert_card(self,card):
        self.__current_state.insert_card(card)

    def load_data(self,card,user_id):
        self.__current_state.load_data(card,user_id)

    def select_operation(self, operation):
        self.__current_state.select_operation(operation)

    def show_current_state(self):
        print(self.__current_state)

    def enter_pin(self,pin):
        self.__current_state.enter_pin(pin)


