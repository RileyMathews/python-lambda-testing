import json

CONFIGURATION = {
    "foo": "bar"
}

def lambda_handler(event, context):
    return {
        "return_message": event["message"],
        "config": CONFIGURATION
    }
