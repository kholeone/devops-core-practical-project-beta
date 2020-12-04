from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestModels(TestBase):
    def test_model(self):
        models = [b'Air Force 1',b'Dunk',b'Air Max 1', b'Air Jordan 1',
		b'Superstar', b'Ultraboost', b'Gazelle', b'Yeezy',
			b'Gel-Lyte III', b'Gel-Lyte V', b'Onitsuka Tiger', b'Gel-Kayano 5'
				b'577', b'998', b'827', b'327']
        response = self.client.get(url_for('shoe_model'))
        self.assertIn(response.data, models)