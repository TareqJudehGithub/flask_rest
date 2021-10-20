
# exercise 1
# class Store:
#     def __init__(self, name):
#         # You'll need 'name' as an argument to this method.
#         # Then, initialise 'self.name' to be the argument, and 'self.items' to 
#         # be an empty list.
#         self.name = name
#         self.items_list = list()
    
    
#     def add_item(self, name, price):
#         # Create a dictionary with keys name and price, and append that to self.items.
#         item_dict = {"name": name, "price": price}
#         self.items_list.append(item_dict)
        

#     def stock_price(self):
#         # Add together all item prices in self.items and return the total.
#         # total = 0
#         # for price in self.items_list:
#         #   total += price["price"]
#         # return total
#         total_price = [sum(item["price"] for item in self.items_list)]
#         for i in total_price:
#           return  i

            
# # instantiate a new obj
# nofal = Store("bread")
# nofal.add_item(name="Banana", price=1.5)
# nofal.add_item(name="Tomato",price=1)
# nofal.add_item(name="Cucumber", price=1)
# print(nofal.stock_price())


# ===================================
print("\n\n")


# exercise 2

# I'm going to code exercise 1 once again just for practice:
class Store:
    def __init__(self, name):
        self.name = name.title()
        self.items = list()
        
    
    def __str__(self):
        return f"Store name is: {self.name}.\n\
Items added: {self.items}\n\
Stock total price = ${self.stock_price()}"
    
    def add_item(self, name, price):
        """Add new items to store function"""

        item_details = {"name": name, "price": price}
        return self.items.append(item_details)
    
    def stock_price(self):
        """Calculate total items price in a store"""
        total_price = sum([item["price"] for item in self.items])
        return total_price
    
    # exercise 2:
     # 1. add a new method called franchise, which creates new franchise stores.

    @classmethod
    def franchise(cls, store):
        "Adding new franchise stores functions"
        return cls(name=store + " - franchise")

    @staticmethod
    def store_details(store):
        return f"{store.name}, total stock price: {store.stock_price()}"
        
   


# Instantiate store_1 from store:
store_1 = Store("Nofal")

# add new item to store_1 using add_item method

milk = store_1.add_item(name="Milk", price=2.99)
bread = store_1.add_item(name="whole wheat bread", price=1)
eggs = store_1.add_item(name="chicken white eggs", price=2)

print(store_1, end="\n")

# total stock price in store_1
print(store_1.stock_price()) 

# franchise stores:

hamudeh = store_1.franchise(store="Hamudeh")
hamudeh.add_item(name="nestle cereal", price=3.75)
hamudeh.add_item(name="pancakes powder", price=4)

print(Store.store_details(hamudeh)) 

print(hamudeh, end="\n")






