# Bridge Pattern

TICKET_PRICE = 10

class TicketBoothWithoutBridge:
    '''
    WithOUT Bridge
    '''

    @staticmethod
    def price(discount_type):
        if discount_type == "STUDENT":
            return TICKET_PRICE - 1        # $1 discount
        elif discount_type == "SENIOR":
            return TICKET_PRICE - 2       # $2 discount
        elif discount_type == "MILITARY":
            return TICKET_PRICE - 3       # $3 discount
        elif discount_type == "VOUCHER":
            return TICKET_PRICE - 4       # $4 discount
        else:
            raise ValueError

print('Student price:', TicketBoothWithoutBridge.price(discount_type="STUDENT"))

# -------------------------------

class TicketBooth:
    '''
    With Bridge
    '''

    @staticmethod
    def price(discount):
        return TICKET_PRICE - discount.AMOUNT

class StudentDiscount:
    AMOUNT = 1

class SeniorDiscount:
    AMOUNT = 1

class MilitaryDiscount:
    AMOUNT = 1

class VoucherDiscount:
    AMOUNT = 1

print('Student price:', TicketBooth.price(discount=StudentDiscount))