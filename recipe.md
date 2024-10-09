## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

----with twilio---
As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ Menu                       │
│                            │
│ - items list               │
│ - cart dict                │
│ - view(all items)          │
│ - add to cart(item)        │
│ - view cart                │
│ - recieve text confirmation│
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Items(title,description,│
│               price)    │
│                         │
│ - title                 │
│ - description           │
│ - price                 │
└─────────────────────────┘
            │
            │ menu uses
            ▼
┌─────────────────────────┐
│ Text()                  │
│                         │
│ - api get request       │
│ - message formatter     │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python


class Menu:
    # User-facing properties:
    #   menu items: dictionary of items and prices
    #   cart: dictionary of cart items, qty and price

    def __init__(self):
         # Parameters:
         #   menu items: a dictionary of menu items and prices
         #   cart: nested dictionary of cart items, qty and price
        pass # No code here yet

    def view_menu(self):
        # Parameters:
        #   menu dict: a dictionary displaying all menu items
        # Side-effects:
        #   Return the dictionary in a viewable format
        pass # No code here yet

    def add_to_cart(self,item):
        # Parameters:
        #   item: string
        # Side effect:
        #   Adds the specified item to the cart dictionary
        pass # No code here yet
    
    def view_cart(self):
        # Parameters:
        #   cart: a formatted list of items, qty, price
        #   total: The grand total of the cart
        # Side effect:
        #   Formats the cart dictionary into a readable format with items, qty and price
        # Returns the formatted cart as wll as a grand total
        pass # No code here yet

    def recieve_text(self, number):
        # Parameters:
        #  number: phone number to send text to
        # Side effect:
        #   Uses the text class to send a text message confirming the order
        pass # No code here yet


class SendText:
    # User-facing properties:
    #  number: phone number passed in by user

    def __init__(self, number):
         # Parameters:
        #  number: phone number passed in by user
        pass # No code here yet

    def get_request(self):
        # Parameters:
        #  none
        # Side effect:
        #   Uses the twilio package to send a text message to the number provided confirming the order
        pass # No code here yet
        
    def format_text(self):
         # Parameters:
        #  none
        # Side effect:
        #   Calls the get_request with the provided number
        pass # No code here yet




```

## 3. Create Examples as UNIT Tests

```python
# EXAMPLE

"""
Given a menu
When we add two items to cart
We see those items reflected in the cart dictionary
"""
menu = Menu()
menu.view_menu() # => {"Ham sandwhich": 1.99, "Cheese panini": 2.29}
menu.add_to_cart('Ham sandwhich')
menu.add_to_cart('Cheese panini')
menu.add_to_cart('Cheese panini')
menu.view_cart() # => {"Ham sandwhich":{
                    # Qty: 1,
                    # Price: 1.99 },
                    #"Cheese panini":{
                    # Qty: 2,
                    # Price: 4.58 },
                    #Total: 6.57}


```

## 4. Create Examples as INTEGRATION Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a menu
When we call receive text
The inputted number recieves a text
"""
menu = Menu()
menu.receive_text(123456) # => 123456 will receive text - "Thank you! Your order was placed and will be delivered before 18:52"
new_text = Text(123456)
Text.format_text()
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._

