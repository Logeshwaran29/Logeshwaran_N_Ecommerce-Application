from entity.customer import Customer
from entity.product import Product
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl


class EcomApp:

    def __init__(self):
        self.method = OrderProcessorRepositoryImpl()

    def register_customer(self):
        print("\n--- Register Customer ---")
        custId = int(input("Enter customer id:"))
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        customer = Customer(custId, name, email, password)
        if self.method.createCustomer(customer):
            print("Customer registered successfully.")
        else:
            print("Customer registration failed.")

    def create_product(self):
        print("\n--- Create Product ---")
        productID = int(input("Enter product id:"))
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        description = input("Enter description: ")
        stock_quantity = int(input("Enter stock quantity: "))
        product = Product(productID, name, price, description, stock_quantity)
        if self.method.createProduct(product):
            print("Product created successfully.")
        else:
            print("Product creation failed.")

    def delete_product(self):
        print("\n--- Delete Product ---")
        product_id = int(input("Enter product ID to delete: "))
        if self.method.deleteProduct(product_id):
            print("Product deleted successfully.")
        else:
            print("Product deletion failed.")

    def add_to_cart(self):
        print("\n--- Add to Cart ---")
        print("--- Product List ---")
        res = self.method.viewProducts()
        c = 0
        for i in res:
            print(f'''{c}: ''', i)
            c += 1
        custId = int(input("\nEnter your customer ID: "))
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        customer = Customer(custId, name, email, password)
        op = int(input("Enter option from List: "))
        quantity = int(input("Enter quantity: "))
        product = Product(res[op][0], res[op][1], res[op][2], res[op][3], res[op][4])
        if self.method.addToCart(customer, product, quantity):
            print("Added to cart successfully.")
        else:
            print("Failed to add to cart.")

    def view_cart(self):
        print("\n--- View Cart ---")
        custId = int(input("Enter your customer ID: "))
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        customer = Customer(custId, name, email, password)
        cartItems = self.method.getAllFromCart(customer)
        print("Cart Items:")
        for i in cartItems:
            print(i)

    def place_order(self):
        print("\n--- Place Order ---")
        print("--- Product List ---")
        res = self.method.viewProducts()
        c = 0
        for i in res:
            print(f'''{c}: ''', i)
            c += 1
        custId = int(input("\nEnter your customer ID: "))
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        customer = Customer(custId, name, email, password)
        op = int(input("Enter option from List: "))
        quantity = int(input("Enter quantity: "))
        product = Product(res[op][0], res[op][1], res[op][2], res[op][3], res[op][4])
        orderProducts = [[product, quantity]]
        shipping_address = input("Enter shipping address: ")
        if self.method.placeOrder(customer, orderProducts, shipping_address):
            print("Order placed successfully.")
        else:
            print("Failed to place order.")

    def view_customer_orders(self):
        print("\n--- View Customer Orders ---")
        customer_id = int(input("Enter your customer ID: "))
        orders = self.method.getOrdersByCustomer(customer_id)
        print("Customer Orders:")
        for i in orders:
            print(i)

    def shop(self):
        while True:
            print("\n1. Register Customer")
            print("2. Create Product")
            print("3. Delete Product")
            print("4. Add to Cart")
            print("5. View Cart")
            print("6. Place Order")
            print("7. View Customer Orders")
            print("0. Exit")
            option = int(input('Enter Option:'))

            if option == 1:
                self.register_customer()
            elif option == 2:
                self.create_product()
            elif option == 3:
                self.delete_product()
            elif option == 4:
                self.add_to_cart()
            elif option == 5:
                self.view_cart()
            elif option == 6:
                self.place_order()
            elif option == 7:
                self.view_customer_orders()
            elif option == 0:
                return
            else:
                print('Enter Correct Option...')


if __name__ == "__main__":
    app = EcomApp()
    app.shop()
