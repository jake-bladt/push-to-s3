import json

class EventProperties:

    @classmethod
    def from_json(cls, json_text):
        obj = json.loads(json_text)
        return cls(obj)

    def __init__(self, event):

        first_record = event['Records'][0]
        repository_arn = first_record['eventSourceARN']

        self.repository_arn = repository_arn
        self.repository_name = repository_arn.split(":")[-1]
        self.last_commit_id = event['Records'][0]['codecommit']['references'][0]['commit']
