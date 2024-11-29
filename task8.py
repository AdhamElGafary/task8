# tests/test_models.py
import unittest
from models import Product  # Assuming your Product model is in the models.py file
from faker import Faker

fake = Faker()

class TestProductModel(unittest.TestCase):

    def test_find_by_availability(self):
        # Create and save multiple available products
        available_products = []
        for _ in range(5):
            product = Product(name=fake.company(),
                              description=fake.text(max_nb_chars=200),
                              price=99.99,
                              sku=fake.uuid4(),
                              category=fake.word(),
                              available=True)  # Assuming availability is a boolean field
            product.save()  # Assuming the 'save' method persists the product
            available_products.append(product)

        # Create and save multiple unavailable products
        for _ in range(5):
            product = Product(name=fake.company(),
                              description=fake.text(max_nb_chars=200),
                              price=99.99,
                              sku=fake.uuid4(),
                              category=fake.word(),
                              available=False)  # Assuming availability is a boolean field
            product.save()

        # Simulate the "find by availability" operation
        found_products = Product.find_by_availability(True)  # Assuming 'find_by_availability' method fetches products by availability

        # Check that the correct number of products are found
        self.assertEqual(len(found_products), len(available_products))

        # Check that each found product is available
        for product in found_products:
            self.assertTrue(product.available)

if __name__ == '__main__':
    unittest.main()
