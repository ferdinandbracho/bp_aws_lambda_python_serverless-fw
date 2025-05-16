import json

import requests
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext

from config import Settings

# Initialize Logger and Tracer
# POWERTOOLS_SERVICE_NAME is automatically picked up by Powertools
logger = Logger()
tracer = Tracer()


@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def initial_function(event: dict, context: LambdaContext) -> dict:
    # Log event and context summaries
    logger.info(f"Event keys: {list(event.keys())}")
    logger.info(f"Context function: {context.function_name}")

    settings = Settings()
    logger.info(f"App: {settings.APP_NAME}, LogLevel: {settings.LOG_LEVEL}")
    dummy_users_text = "[]"  # Default

    try:
        with tracer.capture_subsegment("## get_dummy_users") as subsegment:
            api_url = settings.DUMMY_API_URL
            subsegment.put_metadata("event_summary", str(event)[:200])
            subsegment.put_annotation("api_url", api_url)
            subsegment.put_annotation("service", "jsonplaceholder")

            logger.info("Fetching dummy users from external API.")
            dummy_users_response = requests.get(api_url)
            dummy_users_response.raise_for_status()
            dummy_users_text = dummy_users_response.text
            logger.info("Successfully fetched dummy users.")

        message_part1 = f"{settings.APP_NAME} says: Hello World!"
        message_part2 = "Function executed successfully, with Powertools!"
        
        response_body = {
            'message': f"{message_part1} {message_part2}",
            'dummy_users': dummy_users_text
        }
        return {
            'statusCode': 200,
            'body': json.dumps(response_body)
        }

    except requests.exceptions.RequestException as e:
        logger.exception("HTTP request to external API failed.")
        error_body = {'message': 'Failed to fetch data', 'error': str(e)}
        return {
            'statusCode': 500,
            'body': json.dumps(error_body)
        }
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        error_body = {'message': 'Internal server error', 'error': str(e)}
        return {
            'statusCode': 500,
            'body': json.dumps(error_body)
        }
