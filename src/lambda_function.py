import json

CONFIGURATION = {
    "foo": "bar"
}

def lambda_handler(event, context):
    # TODO implement
    return {
        "return_message": event["message"],
        "config": CONFIGURATION
    }
