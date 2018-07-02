import json
import logging

from pynamodb.exceptions import DoesNotExist

from mthere.models import User


def update(event, context):
    body = json.loads(event['body'])
    user_id = event['pathParameters']['id']
    if 'email' not in body:
        logging.error('Validation Failed %s', body)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t update the user.'})}

    try:
        found_user = User.get(hash_key=user_id)
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'User was not found'})}

    user_changed = False
    # This code from the example seems very repetitive.
    # TODO: replace with a loop
    if body['email'] != found_user.email:
        found_user.email = body['email']
        user_changed = True
    if 'events_invited_to' in body and body['events_invited_to'] != found_user.events_invited_to:
        found_user.events_invited_to = body['events_invited_to']
        user_changed = True
    if 'events_accepted' in body and body['events_accepted'] != found_user.events_invited_to:
        found_user.events_accepted = body['events_accepted']
        user_changed = True
    if 'events_declined' in body and body['events_declined'] != found_user.events_declined:
        found_user.events_declined = body['events_declined']
        user_changed = True
    if 'events_maybe' in body and body['events_maybe'] != found_user.events_maybe:
        found_user.events_maybe = body['events_maybe']
        user_changed = True

    if user_changed:
        found_user.save()
    else:
        logging.info('Nothing changed, did not update')

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(found_user.to_dict(), default=str)}

