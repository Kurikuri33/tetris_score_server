import unittest
import requests
import json

from ..src import score_evaluation_message_pb2

class TestPostAPI(unittest.TestCase):
    def setUp(self):
        with open("api_to_sqs_lambda/infrastructure.json", "r", encoding="utf-8") as f:
            infras = json.load(f)
        self.infra = infras
        return super().setUp()
    
    def test_normal(self):
        msg = score_evaluation_message_pb2.ScoreEvaluationMessage()
        msg.repository_url = "https://github.com/seigot/tetris"
        msg.branch_name = "master"
        msg.game_level = 1
        msg.drop_interval = 1000
        msg.machine_learning_mode = 1
        res = requests.post(f'{self.infra["api_endpoint_url"]["value"]}/score_evaluation', data=msg.SerializeToString())
        response = json.loads(res.text)
        self.assertEqual(response["code"], 200)

if __name__ == '__main__':
    unittest.main()