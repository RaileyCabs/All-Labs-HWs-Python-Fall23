# Lab 11
# Author: James Railey Cabrera

# Lab 11 will show basic understanding of Object Oriented Programming in Python.

import tabulate 

# 1. Create a class called Product.
class Product:
    def __init__(self, name, price, product_id):
        # Attributes for the Product class
        self.name = name
        self.price = price
        self.product_id = product_id

    def __str__(self):
        # Method to represent Product as a string
        return f"Product: {self.name}, Price: {self.price}, ID: {self.product_id}"

# 3. Create a class called Customer.
class Customer:
    def __init__(self, name: str, customer_id: int):
        # Attributes for the Customer class
        self.name = name
        self.customer_id = customer_id
        self.cart = []

    def __str__(self):
        # Method to represent Customer as a string
        return f"Customer: {self.name}, ID: {self.customer_id}"

    def add_to_cart(self, product: Product):
        # Method to add a product to the customer's cart
        self.cart.append(product)
        print(f"{product} was added to {self.name}'s cart")

    def remove_from_cart(self, product: Product):
        # Method to remove a product from the customer's cart
        self.cart.remove(product)
        print(f"{product} was removed from {self.name}'s cart")

    def checkout(self):
        # Method to calculate the total price of products in the cart and print the total
        total = sum(product.price for product in self.cart)
        print(f"{self.name}'s Total: {total}")
        self.cart = []    

    def display_products(self):
        # Method to display products in the customer's cart
        print(f"{self.name}'s Cart:")
        for product in self.cart:
            print(product)
    
    def display_products_pretty(self):
        # Method to display products in the customer's cart using the tabulate library
        print(f"{self.name}'s Cart:")
        table = []
        for product in self.cart:
            table.append([product.name, product.price, product.product_id])
        print(tabulate.tabulate(table, headers=["Name", "Price", "ID"], tablefmt="fancy_grid"))

# 7. Create a class called Store.
class Store:
    def __init__(self):
        # Attributes for the Store class
        self.products = []
        self.customers = []

    def add_product(self, product: Product):
        # Method to add a product to the store
        self.products.append(product)
        print(f"{product} was added to the store")

    def add_customer(self, customer: Customer):
        # Method to add a customer to the store
        self.customers.append(customer)
        print(f"{customer} was added to the store")

    def display_products(self):
        # Method to display products in the store
        print("Products:")
        for product in self.products:
            print(product)

    def display_customers(self):
        # Method to display customers in the store
        print("Customers:")
        for customer in self.customers:
            print(customer)

# 12. Create a store object called store.
store = Store()

# 13. Create a product object called product1 with the following attributes:
product1 = Product("iPhone 12", 799.99, 1)
product2 = Product("iPhone 12 Pro", 999.99, 2)
product3 = Product("iPhone 12 Pro Max", 1099.99, 3)

# 14. Create a product object called product2 with the following attributes:

# 15. Create a product object called product3 with the following attributes:

# 16. Create a customer object called customer1 with the following attributes:
customer1 = Customer("John", 1)
customer2 = Customer("Jane", 2)

# 17. Create a customer object called customer2 with the following attributes:

# 18. Add product1 to the store using the add_product method.
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

# 19. Add product2 to the store using the add_product method.

# 20. Add product3 to the store using the add_product method.

# 21. Add customer1 to the store using the add_customer method.
store.add_customer(customer1)
store.add_customer(customer2)

# 22. Add customer2 to the store using the add_customer method.

# 23. Add product1 to customer1's cart using the add_to_cart method.
customer1.add_to_cart(product1)
customer1.add_to_cart(product2)
customer2.add_to_cart(product3)
# 24. Add product2 to customer1's cart using the add_to_cart method.

# 25. Add product3 to customer2's cart using the add_to_cart method.

# 26. Display current products in customer1's cart using the display_products method.
customer1.display_products_pretty()
customer2.display_products_pretty()

# 27. Display current products in customer2's cart using the display_products method.

# 28. Checkout customer1's cart using the checkout method.
customer1.checkout()
customer2.checkout()
# 29. Checkout customer2's cart using the checkout method.

# 30. Display current products in customer1's cart using the display_products method. (should be empty)
customer1.display_products_pretty()
