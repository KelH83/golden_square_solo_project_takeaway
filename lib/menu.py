from lib.send_text import SendText

class Menu:

    def __init__(self):
        self.menu_items = {
            "ham sandwhich": 1.99,
            "cheese panini": 2.29,
            "tomato soup": 1.50,
            "caesar salad": 1.75
            }
        self.cart = {}

    def view_menu(self):
        return self.menu_items

    
    def add_to_cart(self,item):
        if item in self.cart:
            self.cart[item]["qty"] = self.cart[item]["qty"]+1
        else:
            self.cart[item] = {
                "qty": 1,
                "price":self.menu_items[item]
            }
    
    def view_cart(self):
        total = 0
        for cart_item in self.cart:
            qty_num = self.cart[cart_item]["qty"]
            while qty_num > 0:
                total += self.cart[cart_item]["price"]
                qty_num -= 1
        formatted_cart = [self.cart,{"total": total}]
        return formatted_cart



    def recieve_text(self, number):
        new_text = SendText(number)
        # new_text.number()
        return f"Text will be sent to {number}"
