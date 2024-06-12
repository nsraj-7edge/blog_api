import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BlogPosts')

def list_posts(event, context):
    response = table.scan()
    items = response.get('Items', [])
    
    response = {
        'statusCode': 200,
        'body': json.dumps(items),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
    
    return response
