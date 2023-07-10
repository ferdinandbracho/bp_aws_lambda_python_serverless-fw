import json

from requests import get

from config import config


def initial_function(event, context):
    """
    initial function
    This initial function use requests package to get dummy users.

    Return
        - Dummy message
        - Event object
        - Requested dummy users
        - Config object

    Modify this to fit your needs!

    """

    dummy_users = get('https://jsonplaceholder.typicode.com/users')

    body = {
        'message': 'This is a message from lambda deployed using serverless',
        'input': event,
        'dummy_users': dummy_users.text,
        'env': config.__dict__
    }

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return response

