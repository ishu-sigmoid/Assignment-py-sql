from unittest import TestCase
from ques_2 import Total_compensation


class ProblemTest(TestCase):
    def setUp(self) -> None:
        self.compensation = Total_compensation("cur")

    def tearDown(self) -> None:
        self.compensation = None

    def test_get_result(self):
        self.assertEqual(self.compensation.Total_compensation(), False)