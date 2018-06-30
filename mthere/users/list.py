import json

from mthere.models import User


def list(event, context):
    # fetch all users from the database
    results = User.scan()

    # create a response
    return {'statusCode': 200,
            'body': json.dumps({'items': [dict(result) for result in results]})}
