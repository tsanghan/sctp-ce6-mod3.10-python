# from flask import Flask, jsonify, make_response

# app = Flask(__name__)

# @app.route("/")
# def home(*args):
#     print("From ***ROOT***!!")
#     return jsonify(message='Hello from ***HELLO*** function!')


# @app.route("/hello")
# def hello(*args):
#     print("From ***HELLO***!!")
#     return jsonify(message='Hello from ***HELLO*** function!')


# @app.route("/hello2")
# def hello2(*args):
#     print("From ***HELLO***!!")
#     return jsonify(message='Hello from ***HELLO-2*** function!')


# @app.route("/hello3")
# def hello3(*args):
#     print("From ***HELLO***!!")
#     return jsonify(message='Hello from ***HELLO-3*** function!')

import json


def hello(event, context):
    print(f"Your function ***HELLO*** executed successfully! Event={event}, Context={context}")
    body = {
        "message": "Go Serverless v4.0! Your function ***hello*** executed successfully!"
    }

    return {"statusCode": 200, "body": json.dumps(body)}

def hello2(event, context):
    print(f"Your function ***HELLO-2*** executed successfully! Event={event}, Context={context}")
    body = {
        "message": "Go Serverless v4.0! Your function ***hello-2*** executed successfully!"
    }

    return {"statusCode": 200, "body": json.dumps(body)}

def hello3(event, context):
    print(f"Your function ***hello3*** executed successfully! Event={event}, Context={context}")
    body = {
        "message": "Go Serverless v4.0! Your function ***hello-3*** executed successfully!"
    }

    return {"statusCode": 200, "body": json.dumps(body)}