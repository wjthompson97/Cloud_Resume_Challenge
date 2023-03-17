import unittest
from unittest.mock import MagicMock
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def setUp(self):
        self.event = {}
        self.context = MagicMock()

def test_lambda_handler(self):
        table_mock = MagicMock()
        table_mock.get_item.return_value = {'Item': {'visitcounter': '1'}}
        table_mock.put_item.return_value = {}
        dynamodb_mock = MagicMock(resource=MagicMock(return_value=table_mock))
        boto3_mock = MagicMock(resource=dynamodb_mock)

        # Invoke lambda_handler with the mock inputs
        response = lambda_handler(self.event, self.context, boto3_mock)

        # Assert that the response is as expected
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], '2')

        # Assert that the DynamoDB methods were called with the expected parameters
        table_mock.get_item.assert_called_once_with(Key={'ID': 'visit'})
        table_mock.put_item.assert_called_once_with(Item={'ID': 'visit', 'visitcounter': '2'})

        # Return a message indicating whether the test passed or failed
        if self.failureCount == 0:
            return "All tests passed"
        else:
            return "Some tests failed"
