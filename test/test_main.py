from src.lambda_function import lambda_handler


class TestHandler(object):
    def test_can_return_message(self):
        event = {"message": "This is a test message"}
        assert lambda_handler(event, None) == {
            "return_message": "This is a test message",
            "config": {"foo": "bar"},
        }
