

class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to 
        # be an empty list.
        self.name = name
        self.items_list = list()
    
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item_dict = {"name": name, "price": price}
        self.items_list.append(item_dict)
        

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        # total = 0
        # for price in self.items_list:
        #   total += price["price"]
        # return total
        total_price = [sum(item["price"] for item in self.items_list)]
        for i in total_price:
          return  i

            
          



# instantiate a new obj
nofal = Store("bread")
nofal.add_item(name="Banana", price=1.5)
nofal.add_item(name="Tomato",price=1)
nofal.add_item(name="Cucumber", price=1)
print(nofal.stock_price())

