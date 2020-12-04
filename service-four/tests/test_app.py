from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPrice(TestBase):
      def test_af1_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='Nike Air Force 1',
        
        )
        self.assertIn(b'84.95', response.data)

      def test_d_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='Nike Dunk',
        
        )
        self.assertIn(b'84.95', response.data)

      def test_am1_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='Nike Air Max 1',
        
        )
        self.assertIn(b'99.95', response.data)

      def test_aj1_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='Nike Air Jordan 1',
        
        )
        self.assertIn(b'135.0', response.data)

      def test_as_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='Adidas SuperStar',
        
        )
        self.assertIn(b'80.0', response.data)

      def test_aub_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='Adidas Ultraboost',
        
        )
        self.assertIn(b'139.95', response.data)

      def test_ag_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='Adidas Gazelle',
        
        )
        self.assertIn(b'70.0', response.data)

      def test_ay_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='Adidas Yeezy',
        
        )
        self.assertIn(b'179.95', response.data)

      def test_agl3_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='Asics Gel Lyte-III',
        
        )
        self.assertIn(b'95.0', response.data)
    
      def test_agl5_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='Asics Gel Lyte-V',
        
        )
        self.assertIn(b'100.0', response.data)

      def test_aot_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='Asics Onitsuka Tiger',
        
        )
        self.assertIn(b'75.0', response.data)

      def test_agk5_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='Asics Gel-Kayano 5',
        
        )
        self.assertIn(b'115.0', response.data)

      def test_nb577_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='New Balance 577',
        
        )
        self.assertIn(b'150.0', response.data)

      def test_nb998_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='New Balance 998',
        
        )
        self.assertIn(b'200.0', response.data)

      def test_nb827_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='New Balance 827',
        
        )
        self.assertIn(b'100.0', response.data)

      def test_nb327_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='New Balance 327',
        
        )
        self.assertIn(b'80.0', response.data)

      def test_nonexistent_price(self):
        response =self.client.post(
            url_for('shoe_price'),
            data='',
        
        )
        self.assertIn(b'This trainer does not exist!', response.data)
