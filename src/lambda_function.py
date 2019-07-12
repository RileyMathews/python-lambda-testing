import json
import sys

CONFIGURATION = {"foo": "bar"}


def lambda_handler(event, context):
    return getattr(sys.modules[__name__], event["method"])(event["first_number"], event["second_number"])

def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second