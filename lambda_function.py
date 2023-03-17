import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CloudResumeChallenge')

def lambda_handler(event, context):
    
    response = table.get_item (
        Key = {
            'ID':'visit'
        }
    )
        
    visit_count = response['Item']['visitcounter'] #gets the current calue of 'visitor counter
    visit_count = str(int(visit_count) + 1) #increments and converts the value to a string
        
    response = table.put_item ( 
        Item = {
                'ID': 'visit',
                'visitcounter' : visit_count
            }
        )

    return {
        'statusCode': 200, #sets the HTTP status code to 200 OK
        'headers': {
            'Access-Control-Allow-Headers':'*',
            'Access-Control-Allow-Origin':'*',
            'Access-Control-Allow-Methods':'*'
        }, #sets the HTTP response headers for CORS *IMPORTANT*
        'body':visit_count #sets the HTPP response body to the value of visit_count
    }

