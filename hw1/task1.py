"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""

class CashRegister:

    def __init__(self):

        self.total_items = {}  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item_and_price):
        self.total_items.update(item_and_price)

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, monetary_amount):
        self.discount += monetary_amount

    def get_total(self):
        total_before_discount = sum(self.total_items.values())
        return total_before_discount - self.discount

    def show_items(self):
        for item, price in self.total_items.items():
            print(f" - {item} - £{price:.2f}")

    def reset_register(self):
        self.total_items = {}
        self.total_price = 0
        self.discount = 0

# Shop has 3 cash registers
register_1 = CashRegister()
register_2 = CashRegister()
register_3 = CashRegister()

# Add item - Customer at cash register 1 would like to buy milk, bread and butter
register_1.add_item({'Milk': 2.00})
register_1.add_item({'Bread': 1.25})
register_1.add_item({'Butter': 1.50})

# Remove item - Customer no longer wants to buy butter
register_1.remove_item('Butter')

# Apply discount - Customer has a £1 off discount code for milk
register_1.apply_discount(1.00)

# Get total - Customer would like to see the total cost of their items
print(register_1.get_total())

# Show items - Customer would like to see all the items they have added
register_1.show_items()

# Reset register - Customer checks out and new one arrives
register_1.reset_register()