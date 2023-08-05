import unittest
from EventProperties import EventProperties

import json

class TestEventPropertiesCase(unittest.TestCase):

    def test_initialize(self):
        sample_json = """{
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
}"""

        props = EventProperties.from_json(sample_json)
        self.assertEqual(props.repository_arn, "arn:aws:codecommit:us-east-1:614218673609:jbcodes-ui")
        self.assertEqual(props.repository_name, "jbcodes-ui")
        self.assertEqual(props.last_commit_id, "5570d84dacb6b34ae81ea033caf0dcb289a79163")

    def test_initialize_multicommit(self):
        sample_json = """{
    "Records": [
        {
            "awsRegion": "us-east-1",
            "codecommit": {
                "references": [
                    {
                        "commit": "d40e64d275ee2af95e80de3d21d0fc652406b385",
                        "ref": "refs/heads/main"
                    }
                ]
            },
            "customData": null,
            "eventId": "93fc45f2-f850-430d-90ef-9f137d3a018e",
            "eventName": "ReferenceChanges",
            "eventPartNumber": 1,
            "eventSource": "aws:codecommit",
            "eventSourceARN": "arn:aws:codecommit:us-east-1:614218673609:jbcodes-ui",
            "eventTime": "2023-08-05T19:36:05.440+0000",
            "eventTotalParts": 1,
            "eventTriggerConfigId": "11369698-efd0-4dd5-86d7-5498710d1812",
            "eventTriggerName": "jbcodes-ui_update",
            "eventVersion": "1.0",
            "userIdentityARN": "arn:aws:iam::614218673609:user/jake-code-admin"
        }
    ]
}"""

        props = EventProperties.from_json(sample_json)
        self.assertEqual(props.repository_arn, "arn:aws:codecommit:us-east-1:614218673609:jbcodes-ui")
        self.assertEqual(props.repository_name, "jbcodes-ui")
        self.assertEqual(props.last_commit_id, "d40e64d275ee2af95e80de3d21d0fc652406b385")


    def test_fail_on_bad_structure(self):
        bad_event = {
            'Records': [ { 'awsregion': 'us-north-1' } ]
        }
        with self.assertRaises(KeyError):
            props = EventProperties(bad_event)


if __name__ == '__main__':
    unittest.main()
