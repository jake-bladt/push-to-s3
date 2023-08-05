import boto3
import datetime
import json

from EventProperties import EventProperties

def handler(event, context):
    timestamp = datetime.datetime.utcnow().isoformat()
    print('Timestamp = ' + timestamp)

    event_props = EventProperties(event)

    s3 = boto3.resource('s3')
    block_key= timestamp + '.txt'
    obj = s3.Object(bucket_name='jbc-cicd-poc', key=block_key)
    obj.put(Body=event_props.commit_id)
