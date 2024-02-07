class Fruit:

  def __init__(self, id, name, price, quantity, origin):
    self._id = id
    self._name = name
    self._price = price
    self._quantity = quantity
    self._origin = origin

  @property
  def id(self):
    return self._id

  @id.setter
  def id(self, value):
    self._id = value

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    self._name = name

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, price):
    self._price = price

  @property
  def quantity(self):
    return self._quantity

  @quantity.setter
  def quantity(self, quantity):
    self._quantity = quantity

  @property
  def origin(self):
    return self._origin

  @origin.setter
  def origin(self, origin):
    self._origin = origin

  def __repr__(self):
    return f"| {self.id:^11} | {self.name:^17} | {self.origin:^12} | {self.price:^13}$ |"
