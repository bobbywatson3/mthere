import json

from pynamodb.exceptions import DoesNotExist
from mthere.models import User


def get(event, context):
    try:
        found_user = User.get(hash_key=event['pathParameters']['id'])
    except (DoesNotExist, KeyError):
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'User was not found'})}

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(found_user.to_dict(), default=str)}