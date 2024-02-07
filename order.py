class Order:
  _order_id_system = 0

  def __init__(self, customer_name, fruit_cart=None):
    Order._order_id_system += 1
    self._order_id = Order._order_id_system
    self._customer_name = customer_name
    self._fruit_cart = fruit_cart if fruit_cart is not None else []

  @property
  def order_id(self):
    return self._order_id

  @classmethod
  def get_maximum_order_id(cls):
    return cls._order_id_system

  @property
  def customer_name(self):
    return self._customer_name

  @customer_name.setter
  def customer_name(self, customer_name):
    self._customer_name = customer_name

  @property
  def fruit_cart(self):
    return self._fruit_cart
