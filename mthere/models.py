import os
from datetime import datetime

from pynamodb.attributes import ListAttribute, UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class User(Model):
    class Meta:
        table_name = os.environ['DYNAMODB_TABLE']
        # Connect to the local instance of DynamoDB for dev/test
        if 'ENV' in os.environ:
            host = 'http://localhost:8000'
        else:
            region = 'us-east-1'
            host = 'https://dynamodb.us-east-1.amazonaws.com'

    user_id = UnicodeAttribute(hash_key=True)
    # Using shorter names for attr_name, so that we can use
    # longer more descriptive names in code, but shorter names
    # will be stored in DynamoDB (and save us money)
    events_invited_to = ListAttribute(null=True, attr_name='inv')
    events_accepted = ListAttribute(null=True, attr_name='acc')
    events_declined = ListAttribute(null=True, attr_name='dec')
    events_maybe = ListAttribute(null=True, attr_name='may')
    email = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(null=False, default=datetime.now(), attr_name='cre')
    updated_at = UTCDateTimeAttribute(null=False, attr_name='upd')

    def save(self, conditional_operator=None, **expected_values):
        self.updated_at = datetime.now()
        super(User, self).save()

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))
