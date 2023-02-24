class Empty:

    def __init__(self, context):
        self._cart = context

    def add_item(self):
        self._cart.items += 1
        self._cart.state = self._cart.notempty
        print('item added')

    def remove_item(self):
        print("empty cart. can't remove item")

class NotEmpty:

    def __init__(self, context):
        self._cart = context

    def add_item(self):
        self._cart.items += 1
        self._cart.state = self._cart.notempty
        print('item added')

    def remove_item(self):
        self._cart.items -= 1
        if self._cart.items == 0:
            self._cart.state = self._cart.notempty
        print('item removed')


class ShoppingCart:

    def __init__(self):
        self.empty = Empty(self)
        self.notempty = NotEmpty(self)

        self.items = 0
        self.state = self.empty

    def add_item(self):
        self.state.add_item()

    def remove_item(self):
        self.state.remove_item()

shopping_cart = ShoppingCart()
shopping_cart.remove_item()
shopping_cart.add_item()
shopping_cart.add_item()
shopping_cart.add_item()
shopping_cart.remove_item()
