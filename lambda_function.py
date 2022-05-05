import json
import base64
import boto3
from urllib.parse import parse_qs

def lambda_handler(event, context):
    queryparm = parse_qs(base64.b64decode(event["body"]).decode('ascii'))
    state = queryparm['state'][0]
    date = queryparm['date'][0]
    
    s3 = boto3.client('s3')
    resp = s3.select_object_content(
        Bucket = "loa037-cc-final",
        Key = f"covid/{date}.csv",
        Expression = f"SELECT * from S3Object s WHERE Province_State='{state}'",
        ExpressionType = "SQL",
        InputSerialization = {'CSV': {'FileHeaderInfo': 'Use'}},
        OutputSerialization = {'JSON': {}}
    )
    
    record = ""
    for event in resp['Payload']:
        if 'Records' in event:
            print(event['Records']['Payload'].decode())
            record = event['Records']['Payload'].decode()
            
    
    return {
        'statusCode': 200,
        'body': record
    }

