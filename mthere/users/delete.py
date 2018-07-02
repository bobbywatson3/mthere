import json
from pynamodb.exceptions import DoesNotExist, DeleteError

from mthere.models import User


def delete(event, context):
    user_id = event['pathParameters']['id']
    try:
        found_user = User.get(hash_key=user_id)
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'User was not found'})}
    try:
        found_user.delete()
    except DeleteError:
        return {'statusCode': 400,
                'body': json.dumps({'error_message': 'Unable to delete the user'})}

    # create a response
    return {'statusCode': 204}