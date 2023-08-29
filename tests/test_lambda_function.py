import unittest

import lambda_function


class SimpleTest(unittest.TestCase):

    @staticmethod
    def test_lambda_handler():
        event = {}
        context = ""
        response = lambda_function.lambda_handler(event, context)


if __name__ == "__main__":
    unittest.main()
