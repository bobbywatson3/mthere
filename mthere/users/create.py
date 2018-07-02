import json
import logging
import uuid
from datetime import datetime
from mthere.models import User


def create(event, context):
    print(event)
    body = json.loads(event['body'])
    if 'email' not in body or 'user_id' not in body:
        logging.error('Validation Failed')
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the user.'})}

    if not body['email'] or not body['user_id']:
        logging.error('Validation Failed - email was empty. %s', event)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the user. Email address and user_id required.'})}

    user = User(user_id=str(uuid.uuid1()),
                email=body['email'],
                created_at=datetime.now())
    user.save()

    # create a response
    return {'statusCode': 201,
            'body': json.dumps(user.to_dict(), default=str)}