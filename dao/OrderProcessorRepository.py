from abc import ABC, abstractmethod


class OrderProcessorRepository(ABC):
    @abstractmethod
    def createProduct(self, product):
        pass

    @abstractmethod
    def createCustomer(self, customer):
        pass

    @abstractmethod
    def deleteProduct(self, productId):
        pass

    @abstractmethod
    def deleteCustomer(self, customerId):
        pass

    @abstractmethod
    def addToCart(self, customer, product, quantity):
        pass

    @abstractmethod
    def removeFromCart(self, customer, product):
        pass

    @abstractmethod
    def getAllFromCart(self, customer):
        pass

    @abstractmethod
    def placeOrder(self, customer, orderDetails, address):
        pass

    @abstractmethod
    def getOrdersByCustomer(self, customer_id):
        pass

    @abstractmethod
    def viewProducts(self):
        pass
