def handle(event, context):
    return {
        "statusCode": 200,
        "body": str(event.body).upper()
    }
