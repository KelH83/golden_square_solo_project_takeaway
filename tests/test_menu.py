from lib.menu import Menu
from unittest.mock import Mock

lunch_menu = Menu()

def test_creates_instance():
    assert isinstance(lunch_menu, Menu)
    assert lunch_menu.menu_items == {
            "ham sandwhich": 1.99,
            "cheese panini": 2.29,
            "tomato soup": 1.50,
            "caesar salad": 1.75
            }
    assert lunch_menu.cart == {}

def test_view_menu_returns_entire_menu():
    assert lunch_menu.view_menu() == {
            "ham sandwhich": 1.99,
            "cheese panini": 2.29,
            "tomato soup": 1.50,
            "caesar salad": 1.75
            }

def test_add_to_cart_adds_items_to_cart_dictionary():
    lunch_menu.add_to_cart("ham sandwhich")
    lunch_menu.add_to_cart("tomato soup")
    assert lunch_menu.cart == {
        "ham sandwhich":{
            "qty": 1,
            "price": 1.99
        },
        "tomato soup":{
            "qty":1,
            "price": 1.50
        }
        }
    
def test_add_to_cart_updates_qty_for_item_already_in_cart():
    lunch_menu.add_to_cart("tomato soup")
    assert lunch_menu.cart == {
        "ham sandwhich":{
            "qty": 1,
            "price": 1.99
        },
        "tomato soup":{
            "qty":2,
            "price": 1.50
        }
        }
    
def test_view_cart_shows_entire_cart_and_total():
    assert lunch_menu.view_cart() == [
        {"ham sandwhich":{
            "qty": 1,
            "price": 1.99
        },
        "tomato soup":{
            "qty":2,
            "price": 1.50
        }
        },
        {"total": 4.99}
    ]
    
def test_recieve_text_stores_the_given_number():
    assert lunch_menu.recieve_text(123456) == "Text will be sent to 123456"
