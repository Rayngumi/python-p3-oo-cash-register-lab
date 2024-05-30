#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.items.append(title)

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = self.total * (1 - self.discount / 100.0)
      print(f"After the discount, the total comes to ${self.total:.0f}.")

  def void_last_transaction(self):
    if len(self.items) == 0:
      self.total = 0
      print("There are no items to void.")
    else:
      self.total -= self.total / len(self.items)
      self.items.pop()

      
