import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BlogPosts')

def delete_post(event, context):
    post_id = event['pathParameters']['id']
    
    response = table.delete_item(
        Key={'PostID': post_id}
    )
    
    response = {
        'statusCode': 204,
        'body': '',
        'headers': {
            'Content-Type': 'application/json'
        }
    }
    
    return response
