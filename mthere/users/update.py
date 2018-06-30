import json
import logging

from pynamodb.exceptions import DoesNotExist

from mthere.models import User


def update(event, context):
    if 'email' not in event:
        logging.error('Validation Failed %s', event)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t update the user.'})}

    try:
        found_user = User.get(hash_key=event['user_id'])
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'User was not found'})}

    user_changed = False
    # This code from the example seems very repetitive.
    # TODO: replace with a loop
    if 'email' in event and event['email'] != found_user.email:
        found_user.email = event['email']
        user_changed = True
    if 'events_invited_to' in event and event['events_invited_to'] != found_user.events_invited_to:
        found_user.events_invited_to = event['events_invited_to']
        user_changed = True
    if 'events_accepted' in event and event['events_accepted'] != found_user.events_invited_to:
        found_user.events_accepted = event['events_accepted']
        user_changed = True
    if 'events_declined' in event and event['events_declined'] != found_user.events_declined:
        found_user.events_declined = event['events_declined']
        user_changed = True
    if 'events_maybe' in event and event['events_maybe'] != found_user.events_maybe:
        found_user.events_maybe = event['events_maybe']
        user_changed = True

    if user_changed:
        found_user.save()
    else:
        logging.info('Nothing changed, did not update')

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(dict(found_user))}

