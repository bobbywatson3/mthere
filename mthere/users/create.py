import json
import logging
import uuid
from datetime import datetime
from mthere.models import User


def create(event, context):
    if 'email' not in event or 'user_id' not in event:
        logging.error('Validation Failed')
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the user.'})}

    if not event['email'] or not event['user_id']:
        logging.error('Validation Failed - email was empty. %s', event)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the user. Email address and user_id required.'})}

    user = User(user_id=str(uuid.uuid1()),
                email=event['email'],
                created_at=datetime.now())

    user.save()
    print(dict(user))

    # create a response
    return {'statusCode': 201,
            'body': json.dumps(dict(user))}