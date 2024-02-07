from fruit import Fruit
from order import Order
from input_data import InputData
from colorama import Fore, Style


class FruitShop:

  def __init__(self):
    self.menu_options = {
        "1": self.create_fruit,
        "2": self.view_orders,
        "3": self.shopping
    }
    self.fruits_list = []
    self.fruits_orders = {}

  def create_fruit(self):
    fruit_id = 1
    while True:
      if self.fruits_list:
        fruit_id = self.fruits_list[-1].id + 1
      fruit_name = InputData.name_input(
          "Enter fruit name: ", "Fruit name", r"^[a-zA-Z ]+$",
          "Fruit name must be letters from a - z")
      if fruit_name is None:
        break
      fruit_price = InputData.float_input("Enter fruit price: ", "Fruit price",
                                          0, 999.99)
      if fruit_price is None:
        break
      fruit_quantity = InputData.int_input("Enter fruit quantity: ",
                                           "Fruit quantity", 0, 999)
      if fruit_quantity is None:
        break
      fruit_origin = InputData.name_input(
          "Enter fruit origin: ", "Fruit origin", r"^[a-zA-Z ]+$",
          "Fruit name must be letters from a - z")
      if fruit_origin is None:
        break
      fruit = Fruit(fruit_id, fruit_name, fruit_price, fruit_quantity,
                    fruit_origin)
      self.fruits_list.append(fruit)
      add_more_choice = input("Do you want to continue (Y/N)? ").upper()
      if add_more_choice == "N":
        self.display_all_fruits()
        break

  def view_orders(self):
    if self.fruits_orders:
      for order_id, order in self.fruits_orders.items():
        print(f"Customer: {order.customer_name}")
        print(f"| {'Product'} | {'Quantity'} | {'Price'} | {'Amount'} |\n")
        for fruit in order.fruit_cart:
          amount = fruit.price * fruit.quantity
          print(
              f"{fruit.name:<8} | {fruit.quantity:<8} | {fruit.price:<5}$ | {amount:<7}$ |"
          )
        print("Total:",
              sum(fruit.price * fruit.quantity for fruit in order.fruit_cart))
        print()
    else:
      print("Order list is empty.")

  def shopping(self):
    print("Shopping")
    if not self.fruits_list:
      print("Shop is having no fruits")
      return

    fruit_cart = self.create_fruit_cart()
    if not fruit_cart:
      print("No fruit selected")
      return

    self.process_order(fruit_cart)

  def create_fruit_cart(self):
    fruit_cart = []
    while True:
      print("List of Fruit:")
      self.display_all_fruits()
      fruit_item_id = InputData.int_input("Enter fruit item number: ",
                                          "Fruit item number", 1,
                                          len(self.fruits_list))
      if fruit_item_id is None:
        break
      fruit_item = self.fruits_list[fruit_item_id - 1]
      fruit_item_copy = Fruit(fruit_item.id, fruit_item.name, fruit_item.price,
                              fruit_item.quantity, fruit_item.origin)
      print(f"You selected: {fruit_item.name}")
      fruit_bought_quantity = InputData.int_input(
          "Please input quantity: ", f"Quantity of {fruit_item.name}", 1,
          fruit_item.quantity)
      if fruit_bought_quantity is None:
        break

      fruit_in_cart = next(
          (f for f in fruit_cart if f.id == fruit_item_copy.id), None)
      if fruit_in_cart:
        total_quantity = fruit_in_cart.quantity + fruit_bought_quantity
        if total_quantity > fruit_item_copy.quantity:
          print(
              f"{Fore.RED}Sorry, the quantity of {fruit_item_copy.name} in your cart ({total_quantity}) exceeds the available quantity in stock ({fruit_item_copy.quantity}). Please enter a valid quantity.{Style.RESET_ALL}"
          )

          continue
        fruit_in_cart.quantity += fruit_bought_quantity
      else:
        fruit_item_copy.quantity = fruit_bought_quantity
        fruit_cart.append(fruit_item_copy)
      order_now_choice = input("Do you want to order now (Y/N)? ").upper()
      if order_now_choice == "Y":
        break
    return fruit_cart

  def process_order(self, fruit_cart):
    self.display_cart(fruit_cart)
    customer_name = InputData.name_input(
        "Input your name: ", "Your Name", r"^[a-zA-Z ]+$",
        "Your name must be letters from a - z")
    if customer_name is None:
      print("Order cancelled")
      return
    new_order = Order(customer_name, fruit_cart)
    self.fruits_orders[new_order.order_id] = new_order

    for fruit_order in fruit_cart:
      for fruit_shop in self.fruits_list:
        if fruit_order.id == fruit_shop.id:
          fruit_shop.quantity -= fruit_order.quantity

    self.fruits_list = [
        fruit_shop for fruit_shop in self.fruits_list
        if fruit_shop.quantity > 0
    ]

    for index, fruit_shop in enumerate(self.fruits_list, start=1):
      fruit_shop.id = index

    print("Order placed successfully!")

  def display_all_fruits(self):
    print(
        f"| {'++ Item ++':^11} | {'++ Fruit Name ++':^17} | {'++ Origin ++':^12} | {'++ Price ++':^13} |"
    )
    for fruit in self.fruits_list:
      print(fruit)

  def display_cart(self, fruit_cart):
    print(
        f"| {'Product':<15} | {'Quantity':<8} | {'Price':<5} | {'Amount':<7} |\n"
    )
    total_amount = 0
    for item in fruit_cart:
      amount = item.price * item.quantity
      print(
          f"| {item.name:<15} | {item.quantity:<8} | {item.price:<5}$ | {amount:<7}$ |\n"
      )
      total_amount += amount

    print(f"{'Total:':<28} {total_amount}$\n")

  def display_menu(self):
    print("""\n=========FRUIT SHOP SYSTEM=========
        1. Create Fruit
        2. View orders
        3. Shopping (for buyer)
        4. Exit

*Enter 'cancel' to cancel enter :)*
    \n""")

  def run(self):
    while True:
      self.display_menu()
      choice = input("Enter your choice: ")
      if choice == "4" or choice == "cancel":
        print("See you.")
        break

      if choice in self.menu_options:
        self.menu_options[choice]()
      else:
        print("Invalid choice. Please try again.")
