import unittest
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from entity.customer import Customer
from entity.product import Product


class TestCases(unittest.TestCase):
    def setUp(self):
        self.method = OrderProcessorRepositoryImpl()
        self.customer = Customer(1, 'loki', 'loki@gmail.com', 'loki123')
        self.product = Product(3, 'Smart Watch', 2000, 'Electronics and Gadgets', 2000)
        self.orderDetails = [[self.product, 10]]

    def test(self):
        res = self.method.createProduct(self.product)
        self.assertEqual(res, True)

    def test1(self):
        res = self.method.addToCart(self.customer, self.product, 5)
        self.assertEqual(res, True)

    def test2(self):
        res = self.method.placeOrder(self.customer, self.orderDetails, 'Chennai')
        self.assertEqual(res, True)

    def test3(self):
        res = self.method.deleteCustomer(3)
        self.assertEqual(res, False)

    def test4(self):
        res = self.method.deleteProduct(4)
        self.assertEqual(res, False)


if __name__ == "__main__":
    unittest.main()
