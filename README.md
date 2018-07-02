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
Serverless: Installing requirements of requirements.txt in .serverless...
Serverless: Docker Image: lambci/lambda:build-python3.6
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Injecting required Python packages to package...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (509.22 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
......................................
Serverless: Stack update finished...
Service Information
service: mthere
stage: dev
region: us-east-1
stack: mthere-dev
api keys:
  None
endpoints:
  POST - https://XXXXXX.execute-api.us-east-1.amazonaws.com/dev/mthere/users
  GET - https://XXXXXX.execute-api.us-east-1.amazonaws.com/dev/mthere/users/{id}
  GET - https://XXXXXX.execute-api.us-east-1.amazonaws.com/dev/mthere/users
  PUT - https://XXXXXX.execute-api.us-east-1.amazonaws.com/dev/mthere/users/{id}
  DELETE - https://XXXXXX.execute-api.us-east-1.amazonaws.com/dev/mthere/users/{id}
functions:
  users_create: mthere-dev-users_create
  users_get: mthere-dev-users_get
  users_list: mthere-dev-users_list
  users_update: mthere-dev-users_update
  users_delete: mthere-dev-users_delete
Serverless: Removing old service versions...
```

## Usage

You can create, retrieve, update, or delete users or events with the following commands:

### Create a User

```bash
curl -H "Content-Type: application/json" -X POST https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/mthere/users -d '{"user_id": "1233446783245", "email": "ash@smart.com"}'
```

Example output:
```bash
{"created_at": "2018-07-02 14:48:21.527201", "user_id": "1233446783245", "email": "ash@smart.com", "updated_at": "2018-07-02 14:48:21.527352"}
```

### List All Users

```bash
curl https://XXXXXX.execute-api.us-east-1.amazonaws.com/dev/mthere/users
```

Example output:
```bash
{"items": [
{"created_at": "2018-06-30 21:46:14.291413+00:00", "updated_at": "2018-06-30 21:46:14.291743+00:00", "email": "test@test.com", "user_id": "02cd0b78-7caf-11e8-9845-d25b2faa1595"}, 
{"created_at": "2018-07-02 14:48:21.527201+00:00", "updated_at": "2018-07-02 14:48:21.527352+00:00", "email": "ash@smart.com", "user_id": "f71858ec-7e06-11e8-9073-c2523bb10998"}, 
]}
```

### Get One User

```bash
# Replace the <id> part with a real id from your users table
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/mthere/users/<id>
```

Example Result:
```bash
{"created_at": "2018-07-02 12:30:51.714929+00:00", "updated_at": "2018-07-02 12:30:51.715280+00:00", "email": "test@test.com", "user_id": "c1d2e35e-7df3-11e8-8b04-ce3128b47469"}
```

### Update a User

```bash
# Replace the <id> part with a real id from your Users table
curl -H "Content-Type: application/json" -X PUT -d '{"email": "newemail@email.com"}' https://XXXXXXX.execute-api.us-east-1.amazonaws.com/users/<id>
```

Example Result:
```bash
{"created_at": "2018-07-02 12:30:51.714929+00:00", "updated_at": "2018-07-02 14:56:19.095179", "email": "newemail@email.com", "user_id": "c1d2e35e-7df3-11e8-8b04-ce3128b47469"}
```

### Delete a User

```bash
# Replace the <id> part with a real id from your users table
curl -X DELETE https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/mthere/users/<id>
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
