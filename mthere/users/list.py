import json

from mthere.models import User


def list(event, context):
    # fetch all users from the database
    results = User.scan()

    # create a response
    return {'statusCode': 200,
            'body': json.dumps({'items': [result.to_dict() for result in results]}, default=str)}
