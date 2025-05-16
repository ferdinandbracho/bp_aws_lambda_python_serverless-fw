import json
from unittest.mock import MagicMock, patch

import pytest
from aws_lambda_powertools.utilities.typing import LambdaContext

# Project root is parent of 'tests', handler.py in root. Pytest finds it.
# Ensure PYTHONPATH correct if run outside pytest (IDE) or config pytest path.
from handler import initial_function


@pytest.fixture
def lambda_event():
    """ Provides a sample API Gateway event """
    return {
        "httpMethod": "GET",
        "path": "/test",
        "queryStringParameters": None,
        "headers": None,
        "body": None,
        "isBase64Encoded": False
    }

@pytest.fixture
def lambda_context() -> LambdaContext:
    """ Provides a mock Lambda context """
    mock_context = MagicMock(spec=LambdaContext)
    mock_context.function_name = "test_initial_function"
    mock_context.memory_limit_in_mb = 128
    mock_context.invoked_function_arn = (
        "arn:aws:lambda:us-east-1:123456789012:function:test_initial_function"
    )
    mock_context.aws_request_id = "c6af9ac6-7b61-11e6-9a41-93e812345678"
    return mock_context


@patch('handler.get')  # Mock 'requests.get' within the handler module
@patch('handler.logger')  # Mock Powertools logger
@patch('handler.tracer')  # Mock Powertools tracer
def test_initial_function_success(
    mock_tracer, mock_logger, mock_requests_get, lambda_event, lambda_context
):
    """ Test successful execution of initial_function """
    # Configure the mock for requests.get
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = json.dumps([{"id": 1, "name": "Test User"}])
    mock_response.raise_for_status = MagicMock()  # Ensure no error
    mock_requests_get.return_value = mock_response

    response = initial_function(lambda_event, lambda_context)

    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert 'Test User' in body['dummy_users']
    assert 'now with Powertools!' in body['message']
    mock_requests_get.assert_called_once_with(
        'https://jsonplaceholder.typicode.com/users'
    )
    mock_logger.info.assert_any_call("Successfully fetched dummy users.")


@patch('handler.get')
@patch('handler.logger')
@patch('handler.tracer')
def test_initial_function_failure_api_call(
    mock_tracer, mock_logger, mock_requests_get, lambda_event, lambda_context
):
    """ Test failure when requests.get raises an exception """
    mock_requests_get.side_effect = Exception("API call failed")

    response = initial_function(lambda_event, lambda_context)

    assert response['statusCode'] == 500
    body = json.loads(response['body'])
    assert body['message'] == 'Failed to fetch data'
    assert 'API call failed' in body['error']
    mock_logger.exception.assert_called_once()
