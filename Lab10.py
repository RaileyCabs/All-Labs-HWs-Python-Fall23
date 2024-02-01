# # Lab 10
# # Author: James Railey Cabrera

# # Lab 10 will show demonstrate how Dictionary's work in Python.

# # 1. Create a dictionary called my_dict with the following key value pairs:
# # Key: "name", Value: "John"
# # Key: "age", Value: 30
# # Key: "city", Value: "Trenton"
# # Key: "state", Value: "New Jersey"
# my_dict = {"name": "John", "age": 30, "city": "Trenton", "state": "New Jersey"}
# # 2. Print out the dictionary.
# print(my_dict)
# # 3. Print out the value for the key "name".
# print(my_dict["name"])
# # 4. Lookup the key associated with the value "New Jersey" and print it out.
# # Hint 1: You will need to loop through the dictionary.
# # Hint 2: remember you can use the .items() method to get the key and value.
# for key, value in my_dict.items():
#     if value == "New Jersey":
#         print(key)
# # 5. Add a new key value pair to the dictionary.
# # Key: "country", Value: "USA"
# my_dict["country"] = "USA"
# # 6. Print out the dictionary.
# print(my_dict)
# # 7. Remove the key value pair with the key "city".
# my_dict.pop("city")
# # 8. Print out the dictionary.
# print(my_dict)
# # 9. Create a dictionary called cities with an key as the City name and values as a list that contains the state, population, and country.
# # use the following data:
# # Trenton, New Jersey, 84,913, USA
# # New York City, New York, 8,336,817, USA
# # Los Angeles, California, 3,979,576, USA
# # Chicago, Illinois, 2,693,976, USA
# # Houston, Texas, 2,320,268, USA
# # Phoenix, Arizona, 1,680,992, USA
# # Philadelphia, Pennsylvania, 1,584,138, USA
# # San Antonio, Texas, 1,547,253, USA
# # San Diego, California, 1,423,851, USA
# cities = {
#     "Trenton": ["New Jersey", 84913, "USA"],
#     "New York City": ["New York", 8336817, "USA"],
#     "Los Angeles": ["California", 3979576, "USA"],
#     "Chicago": ["Illinois", 2693976, "USA"],
#     "Houston": ["Texas", 2320268, "USA"],
#     "Phoenix": ["Arizona", 1680992, "USA"],
#     "Philadelphia": ["Pennsylvania", 1584138, "USA"],
#     "San Antonio": ["Texas", 1547253, "USA"],
#     "San Diego": ["California", 1423851, "USA"],
# }

# # 10. Print a table of the data using the pandas library.
# # pip install pandas
# import pandas as pd

# df = pd.DataFrame.from_dict(cities, orient="index", columns=["State", "Population", "Country"])
# print("-----------------------------------------")
# print(df)


# # 11. Use the tabulate library to print out the table.
# # pip install tabulate
# from tabulate import tabulate

# # 11. Print out the population for the city of Chicago.
# pretty_table = tabulate(df, headers="keys", tablefmt="psql")
# print("-----------------------------------------")
# print(pretty_table)
# print("Population of Chicago: ", df.loc["Chicago"]["Population"])
# # 11. **Extra** An alternative to converting a dictionary into a pandas df then tabulate, you can use dictionary unpacking and tabulate.
# # Dictionary unpacking is a new feature in Python 3.9 and allows you to unpack a dictionary into a list of dictionaries.
# # You can then use tabulate to print out the table.

# # In our case, {"City": city, **info} creates a new dictionary that includes a "City" key with the city name and all the key-value pairs from the info dictionary.

# # For example, if city is "Chicago" and info is {"state": "Illinois", "Population": 2693976, "Country": "USA"}, the new dictionary will be {"City": "Chicago", "state": "Illinois", "Population": 2693976, "Country": "USA"}. This is the same as {"City": city, **info}.
# # The ** operator unpacks the info dictionary into the new dictionary

# # Transform the data

# # Print the table using tabulate


# # 12. How many cities have a population greater than 1 million? Use a for loop to iterate through the dictionary.
# count = 0
# for city, info in cities.items():
#     if info[1] > 1000000:
#         count += 1
# print(f"Cities with population greater than 1 million: {count}")
# # 13.  How many cities are in the USA? Use .items() to get a list of tuples. Use a for loop to iterate through the list of tuples.
# # Hint 1: You will need to use the second item in the tuple. The second item is a dictionary. IE. for city, info in cities.items():
# cities_in_usa = 0
# for city, info in cities.items():
#     if info[2] == "USA":
#         cities_in_usa += 1
# print(f"Cities in USA: {cities_in_usa}")


<<<<<<< HEAD
=======
# 6. Print out the dictionary.

# 7. Remove the key value pair with the key "city".

# 8. Print out the dictionary.

# 9. Create a dictionary called cities with an key as the City name and values as a dictionary that contains the state, population, and country.
# use the following data:
# Trenton, New Jersey, 84,913, USA
# New York City, New York, 8,336,817, USA
# Los Angeles, California, 3,979,576, USA
# Chicago, Illinois, 2,693,976, USA
# Houston, Texas, 2,320,268, USA
# Phoenix, Arizona, 1,680,992, USA
# Philadelphia, Pennsylvania, 1,584,138, USA
# San Antonio, Texas, 1,547,253, USA
# San Diego, California, 1,423,851, USA

# 10. Print a table of the data using the pandas library.
# pip install pandas
>>>>>>> 841429e565bd393572bb285ce262c4e072c54cca




<<<<<<< HEAD
class Product:
    def _init_(self, name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id 
        pass

def _str_(self):
    return f"Product: {self.name}, Price: {self.price}, ID: {self.product_id}"


# 3 customer class 
class Customer: 
    def _init_(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.cart = []  
        pass
=======
# 12. Print out the population for the city of Chicago.


# 13. **Extra** An alternative to converting a dictionary into a pandas df then tabulate, you can use dictionary unpacking and tabulate.
# Dictionary unpacking is a new feature in Python 3.9 and allows you to unpack a dictionary into a list of dictionaries.
# You can then use tabulate to print out the table.
>>>>>>> 841429e565bd393572bb285ce262c4e072c54cca

    def _str_(self):
        return f"Profuct: {self.name}, Price: {self.customer_id}, ID: {self.cart}"
    
    def add_to_cart(self, product:Product):
        self.cart.append(product)
        print(f"{product} was added {self.names} to cart")

    def remove_from_cart(self, product:Product):
        self.cart.remove(product)
        print(f"{product} was removed {self.name}'s cart")


<<<<<<< HEAD

# 6 total price 
    def checkout(self):
        total = 0
        for product in self.cart:
            total += product.price
        print(f"{self.name}'s Total: {total}")
        self.cart = []

    def display_products(self):
        print(f"{self.name}'s Cart:")
        for product in self.cart:
            print(product)
    # 13   

product1 = Product("Apple", 1000.0, 1)
product2 = Product("Orange", 2000.0, 2)
product3 = Product("Banana", 3000.0, 3)

# customers

customer1 = Customer("John", 1)
customer2 = Customer("Jane", 2)

customer1.add_to_cart(product1)
print(customer1.cart)
customer1.add_to_cart(product2)
print(customer1.cart)
customer1.add_to_cart(product3)
print(customer1.cart)
customer1.display_products()
customer1.checkout()

# extra credit tabulate

def display_products_pretty(self):
    import tabulate 

    print(f"{self.name}'s Cart:")
    print(
        [
            {"Name": product.name, "Price": product.price, "ID": product.product_id}
            [product.name, product.price, product.product_id]
            for product in self.cart
        ],
        headers="keys",
        tablefmt="fancy grid",
    )

class store:
    def _init_(self):
        self.products = []
        self.customers = []
    def add_product(self, product:Product):
        self.products.append(product)
        print(f"{product} was added to the store")

def display_products(self):
    print("Products:")
    for product in self.products:
        print(product)

store.add_product(product1)
# print(store)  wont be good need to fix
store.add_product(product2)
store.add_product(product3)

store.add_customer(customer1)
store.add_customer(customer2)

customer1.add_to_cart(product1)
customer1.add_to_cart(product2)
customer2.add_to_cart(product3)

customer1.display_products_pretty()
customer2.display_products()

customer1.checkout
customer2.checkout


# products

product = Product("Apple", 1000.0, 1)
print(product)
=======
# 14. How many cities have a population greater than 1 million? Use a for loop to iterate through the dictionary.

# 15.  How many cities are in the USA? Use .items() to get a list of tuples. Use a for loop to iterate through the list of tuples.
# Hint 1: You will need to use the second item in the tuple. The second item is a dictionary. IE. for city, info in cities.items():
>>>>>>> 841429e565bd393572bb285ce262c4e072c54cca
