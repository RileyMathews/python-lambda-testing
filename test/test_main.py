from src.lambda_function import lambda_handler


class TestHandler(object):
    def test_can_add_numbers(self):
        event = {"method": "add", "first_number": 1, "second_number": 2}
        assert lambda_handler(event, None) == 3

    def test_can_subtract_numbers(self):
        event = {"method": "subtract", "first_number": 5, "second_number": 2}
        assert lambda_handler(event, None) == 3

    def test_can_multiply_numbers(self):
        event = {"method": "multiply", "first_number": 3, "second_number": 2}
        assert lambda_handler(event, None) == 6

    def test_can_divide_numbers(self):
        event = {"method": "divide", "first_number": 6, "second_number": 2}
        assert lambda_handler(event, None) == 3