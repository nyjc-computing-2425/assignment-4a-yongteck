import unittest


from autograding import TestInputOutput, TestFunction
from autograding.case import InOut, FuncCall


class TestNRIC(TestInputOutput):
    def setUp(self):
        self.testcases = [
            InOut(input="T0102051F", output="NRIC is valid."),
            InOut(input="S8521097A", output="NRIC is valid."),
            InOut(input="C1234567C", output="NRIC is invalid."),
            InOut(input="S123456B", output="NRIC is invalid."),
            InOut(input="S1234567A", output="NRIC is invalid."),
        ]


if __name__ == '__main__':
    unittest.main()
