#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items=[]
    self.last_transaction = []


  def add_item(self, title, price, quantity = 1):
    new_price = price * quantity
    new_item = ([title] * quantity)
    self.total = self.total + new_price
    self.items.extend(new_item)
    self.last_transaction = [new_item, new_price]

  
  def apply_discount(self):
    if self.discount > 0:
      discounted_total = self.total - ((self.total * self.discount )* .01) 
      self.total = int(discounted_total)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def items_list(self):
    return self.items

  def void_last_transaction(self):
    self.total = self.total - self.last_transaction[1]

  
