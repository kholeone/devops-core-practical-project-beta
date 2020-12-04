from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestModels(TestBase):
    def test_index_request(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 500)

   







   

    



