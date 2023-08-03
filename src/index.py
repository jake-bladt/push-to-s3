import boto3
import datetime
import json

def get_textfile(fq_path):
    print('Getting' + fq_path)

    cc = boto3.resource('codecommit')
    file_text = cc.get_file()


def handler(event, context):
    timestamp = datetime.datetime.utcnow().isoformat()
    print('Timestamp = ' + timestamp)
    print("Event "  + str(json.dumps(event)))

    commit_id = event['Records'][0]['codecommit']['references'][0]['commit']
    print("Commit id: " + commit_id)

    s3 = boto3.resource('s3')
    block_key= timestamp + '.txt'
    obj = s3.Object(bucket_name='jbc-cicd-poc', key=block_key)
    obj.put(Body=commit_id)
