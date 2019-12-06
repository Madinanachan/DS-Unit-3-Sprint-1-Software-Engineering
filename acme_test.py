import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS
import random


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    def test_default_product_weight(self):
        """Test default weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
    def test_stealability(self):
        prod = Product('Test Product')
        assert (prod.stealability==('Kinda stealable.')|prod.stealability==('Not so stealable...')|prod.stealability==('Very stealable'))

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        prods=generate_products()


if __name__ == '__main__':
    unittest.main()