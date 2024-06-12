import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BlogPosts')

def update_post(event, context):
    body = json.loads(event['body'])
    post_id = event['pathParameters']['id']
    
    title = body['title']
    content = body['content']
    author = body['author']
    
    response = table.update_item(
        Key={'PostID': post_id},
        UpdateExpression="set Title=:t, Content=:c, Author=:a",
        ExpressionAttributeValues={
            ':t': title,
            ':c': content,
            ':a': author
        },
        ReturnValues="UPDATED_NEW"
    )
    
    response_body = response['Attributes']
    response_body['PostID'] = post_id
    
    response = {
        'statusCode': 200,
        'body': json.dumps(response_body),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
    
    return response
