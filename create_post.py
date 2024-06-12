import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BlogPosts')

def create_post(event, context):
    body = json.loads(event['body'])
    
    post_id = str(uuid.uuid4())
    title = body['title']
    content = body['content']
    author = body['author']
    created_at = datetime.utcnow().isoformat()
    
    item = {
        'PostID': post_id,
        'Title': title,
        'Content': content,
        'Author': author,
        'CreatedAt': created_at
    }
    
    table.put_item(Item=item)
    
    response = {
        'statusCode': 201,
        'body': json.dumps(item),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
    
    return response
