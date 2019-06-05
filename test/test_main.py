from src.main import lambda_handler
from unittest import TestCase


class TestHandler(TestCase):
    def test_handler(self):
        self.assertEqual(
            lambda_handler(None, None), {"statusCode": 200, "body": "null"}
        )

    def test_handler_with_args(self):
        self.assertEqual(
            lambda_handler({"test": "value"}, None),
            {"statusCode": 200, "body": '{"test": "value"}'},
        )
