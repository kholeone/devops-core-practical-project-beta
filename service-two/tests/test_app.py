from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestBrands(TestBase):
    def test_brand(self):
        brands = [b'Nike',b'Adidas',b'Asics',b'New Balance']
        response = self.client.get(url_for('shoe_brand'))
        self.assertIn(response.data, brands)