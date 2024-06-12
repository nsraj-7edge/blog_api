import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BlogPosts')

def get_post(event, context):
    post_id = event['pathParameters']['id']
    
    response = table.get_item(
        Key={'PostID': post_id}
    )
    item = response.get('Item', {})
    
    status_code = 200 if item else 404
    
    response = {
        'statusCode': status_code,
        'body': json.dumps(item),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
    
    return response
