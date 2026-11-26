def apply_discount(price, discount):
   if discount < 0 or discount > 100:
       raise ValueError("Discount must be between 0 and 100")
   return price * (1 - discount / 100)