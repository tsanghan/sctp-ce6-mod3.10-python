import unittest
import json
from app import hello, hello2, hello3  # Replace 'your_module' with the actual module name

class TestHelloFunctions(unittest.TestCase):

    def setUp(self):
        # Set up any common test data
        self.event = {"key": "value"}
        self.context = {"function_name": "test"}

    def test_hello(self):
        response = hello(self.event, self.context)
        expected_body = {
            "message": "Go Serverless v4.0! Your function ***hello*** executed successfully!"
        }
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(json.loads(response["body"]), expected_body)

    def test_hello2(self):
        response = hello2(self.event, self.context)
        expected_body = {
            "message": "Go Serverless v4.0! Your function ***hello-2*** executed successfully!"
        }
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(json.loads(response["body"]), expected_body)

    def test_hello3(self):
        response = hello3(self.event, self.context)
        expected_body = {
            "message": "Go Serverless v4.0! Your function ***hello-3*** executed successfully!"
        }
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(json.loads(response["body"]), expected_body)

if __name__ == "__main__":
    unittest.main()
