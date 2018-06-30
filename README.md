# mThere

mThere is a simple RSVP app that allows users to create events and send out invites.
## API
### Users
- POST /users to create user
- PUT /users/id to update user
- DELETE /users/id to delete user
- GET /users/id to get user
- GET /users to get all users (paginated)
### Events
- POST /events to create event
- PUT /events/id to update event
- DELETE /events/id to delete event
- GET /events/id to get event
- GET /events to get all events (paginated)

## Deploy

In order to deploy the app, run

```bash
serverless deploy
```

The expected result should be similar to:

```bash
fill this in
```

## Usage

You can create, retrieve, update, or delete users or events with the following commands:

### Create a User

```bash
curl -X POST https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/users --data '{ "name": "Ash Williams", "email": "ash@smart.com", "password": "Linda" }'
```

No output

### List All Users

```bash
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/users
```

Example output:
```bash
[{"email":"ash@smart.com","id":"ac90fe80-aa83-11e6-9ede-afdfa051af86","events":["520AD8EA-4C5D-4775-AC84-CAEDADB837F0","114143C7-0221-48F0-A292-D50BB7E403EE"]updatedAt":1479139961304},
[{"email":"sam@smart.com","id":"A6B3DC89-A96C-48B1-A7E7-1F377FB0932F","events":["520AD8EA-4C5D-4775-AC84-CAEDADB837F0","DBE9B32E-7146-466E-90BB-27D508A998EE"]updatedAt":1479139961304}]%
```

### Get One User

```bash
# Replace the <id> part with a real id from your todos table
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/users/<id>
```

Example Result:
```bash
{"email":"sam@smart.com","id":"A6B3DC89-A96C-48B1-A7E7-1F377FB0932F","events":["520AD8EA-4C5D-4775-AC84-CAEDADB837F0","DBE9B32E-7146-466E-90BB-27D508A998EE"]updatedAt":1479139961304}%
```

### Update a User

```bash
# Replace the <id> part with a real id from your Users table
curl -X PUT https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/users/<id> --data '{ "email": "ash@smart.com" }'
```

Example Result:
```bash
{"text":"Learn Serverless","id":"ee6490d0-aa81-11e6-9ede-afdfa051af86","createdAt":1479138570824,"checked":true,"updatedAt":1479138570824}%
```

### Delete a Todo

```bash
# Replace the <id> part with a real id from your todos table
curl -X DELETE https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id>
```

No output

## Scaling

### AWS Lambda

By default, AWS Lambda limits the total concurrent executions across all functions within a given region to 100. The default limit is a safety limit that protects you from costs due to potential runaway or recursive functions during initial development and testing. To increase this limit above the default, follow the steps in [To request a limit increase for concurrent executions](http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html#increase-concurrent-executions-limit).

### DynamoDB

When you create a table, you specify how much provisioned throughput capacity you want to reserve for reads and writes. DynamoDB will reserve the necessary resources to meet your throughput needs while ensuring consistent, low-latency performance. You can change the provisioned throughput and increasing or decreasing capacity as needed.

This is can be done via settings in the `serverless.yml`.

```yaml
  ProvisionedThroughput:
    ReadCapacityUnits: 1
    WriteCapacityUnits: 1
```

In case you expect a lot of traffic fluctuation we recommend to checkout this guide on how to auto scale DynamoDB [https://aws.amazon.com/blogs/aws/auto-scale-dynamodb-with-dynamic-dynamodb/](https://aws.amazon.com/blogs/aws/auto-scale-dynamodb-with-dynamic-dynamodb/)
