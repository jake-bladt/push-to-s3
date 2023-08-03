# Lambda function for deploying static sites to S3/CloudFront on checkin to CodeCommit

## Sample Event JSON

```
Event {
    "Records": [
        {
            "awsRegion": "us-east-1",
            "codecommit": {
                "references": [
                    {
                        "commit": "5570d84dacb6b34ae81ea033caf0dcb289a79163",
                        "ref": "refs/heads/main"
                    }
                ]
            },
            "customData": null,
            "eventId": "2bfa10c8-a19a-4946-b321-d4e70c3a42b0",
            "eventName": "ReferenceChanges",
            "eventPartNumber": 1,
            "eventSource": "aws:codecommit",
            "eventSourceARN": "arn:aws:codecommit:us-east-1:614218673609:jbcodes-ui",
            "eventTime": "2023-07-31T16:46:25.647+0000",
            "eventTotalParts": 1,
            "eventTriggerConfigId": "11369698-efd0-4dd5-86d7-5498710d1812",
            "eventTriggerName": "jbcodes-ui_update",
            "eventVersion": "1.0",
            "userIdentityARN": "arn:aws:iam::614218673609:user/jake-code-admin"
        }
    ]
}
```
