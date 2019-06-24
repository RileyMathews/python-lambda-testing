from src.main import lambda_handler
from unittest import TestCase


class TestHandler(TestCase):
    def test_can_return_message(self):
        event = {"message": "This is a test message"}
        self.assertEqual(
            lambda_handler(event, None),
            {"return_message": "This is a test message", "config": {"foo": "bar"}},
        )
