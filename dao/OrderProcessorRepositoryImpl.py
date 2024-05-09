from .OrderProcessorRepository import OrderProcessorRepository
from util.DBConnection import DBConnUtil
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException
from exception.ProductNotFoundException import ProductNotFoundException
from datetime import date


class OrderProcessorRepositoryImpl(OrderProcessorRepository):

    def __init__(self):
        self.connection = DBConnUtil.getConnection()

    def createProduct(self, product):
        try:
            stmt = self.connection.cursor()
            query = '''insert into products values(%s,%s,%s,%s,%s)'''
            data = [product.product_id, product.name, product.price, product.description, product.stockQuantity]
            stmt.execute(query, data)
            self.connection.commit()
            stmt.close()
            return True
        except Exception as e:
            print(e)
            return False

    def createCustomer(self, customer):
        try:
            stmt = self.connection.cursor()
            query = '''insert into customers values(%s,%s,%s,%s)'''
            data = [customer.customer_id, customer.name, customer.email, customer.password]
            stmt.execute(query, data)
            self.connection.commit()
            stmt.close()
            return True
        except Exception as e:
            print(e)
            return False

    def deleteProduct(self, productId):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from products where product_id = {productId}''')
            res = stmt.fetchall()
            if res:
                query = f'''delete from products where product_id = {productId}'''
                stmt.execute(query)
                self.connection.commit()
                stmt.close()
                return True
            else:
                raise ProductNotFoundException('Product Not Found...')
        except Exception as e:
            print(e)
            return False

    def deleteCustomer(self, customerId):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from customers where customer_id = {customerId}''')
            res = stmt.fetchall()
            if res:
                stmt.execute(f'''delete from customers where customer_id = {customerId}''')
                self.connection.commit()
                stmt.close()
                return True
            else:
                raise CustomerNotFoundException('Customer Not Found...')
        except Exception as e:
            print(e)
            return False

    def addToCart(self, customer, product, quantity):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from customers where customer_id = {customer.customer_id}''')
            res = stmt.fetchall()
            if not res:
                raise CustomerNotFoundException('Customer Not Found...')
            stmt.execute(f'''select * from Products where product_id = {product.product_id}''')
            res1 = stmt.fetchall()
            if not res1:
                raise ProductNotFoundException('Product Not Found...')
            query = '''insert into cart(customer_id, product_id, quantity) values(%s, %s, %s)'''
            data = [customer.customer_id, product.product_id, quantity]
            stmt.execute(query, data)
            self.connection.commit()
            stmt.close()
            return True
        except Exception as e:
            print(e)
            return False

    def removeFromCart(self, customer, product):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from customers where customer_id = {customer.customer_id}''')
            res = stmt.fetchall()
            if not res:
                raise CustomerNotFoundException('Customer Not Found...')
            stmt.execute(f'''select * from products where product_id = {product.product_id}''')
            res1 = stmt.fetchall()
            if not res1:
                raise ProductNotFoundException('Product Not Found...')
            stmt.execute(f'''delete from cart where customer_id = {customer.customer_id} 
                        and product_id = {product.product_id}''')
            self.connection.commit()
            stmt.close()
            return True
        except Exception as e:
            print(e)
            return False

    def getAllFromCart(self, customer):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from customers where customer_id = {customer.customer_id}''')
            res = stmt.fetchall()
            if not res:
                raise CustomerNotFoundException('Customer Not Found...')
            query = f'''select b.product_id, name, price, quantity from Products a join
            (select product_id, quantity from cart where customer_id = {customer.customer_id}) as b
            on a.product_id = b.product_id'''
            stmt.execute(query)
            productList = stmt.fetchall()
            stmt.close()
            return productList
        except Exception as e:
            print(e)

    def placeOrder(self, customer, orderDetails, address):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from customers where customer_id = {customer.customer_id}''')
            res = stmt.fetchall()
            if not res:
                raise CustomerNotFoundException('Customer Not Found...')
            totalPrize = orderDetails[0][0].price * orderDetails[0][1]
            orderDate = date.today()
            query = '''insert into orders(customer_id, order_date, total_price, shipping_address) values(%s,%s,%s,%s)'''
            data = [customer.customer_id, orderDate, totalPrize, address]
            stmt.execute(query, data)
            orderID = stmt.lastrowid

            query1 = '''insert into order_items(order_id, product_id, quantity) values(%s,%s,%s)'''
            for i in orderDetails:
                data1 = [orderID, i[0].product_id, i[1]]
                stmt.execute(query1, data1)
            self.connection.commit()
            stmt.close()
            return True
        except Exception as e:
            print(e)
            return False

    def getOrdersByCustomer(self, customer_id):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from customers where customer_id = {customer_id}''')
            res = stmt.fetchall()
            if not res:
                raise CustomerNotFoundException('Customer Not Found...')
            query = f'''select name, quantity from products p join
            (select product_id, quantity from order_items o join 
            (select order_id from orders where customer_id = {customer_id}) as o1
            on o.order_id = o1.order_id) as p1 on p.product_id = p1.product_id'''
            stmt.execute(query)
            Orders = stmt.fetchall()
            stmt.close()
            return Orders
        except Exception as e:
            print(e)
            return []

    def viewProducts(self):
        try:
            stmt = self.connection.cursor()
            stmt.execute('''select * from Products''')
            res = stmt.fetchall()
            stmt.close()
            return res
        except Exception as e:
            print(e)
            return []
