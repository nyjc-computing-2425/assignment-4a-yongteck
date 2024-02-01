import sys
import unittest

# autograding submodule might not be successfully pulled on init
# if unsuccessful, we have to pull it manually
# limit number of retries
MAX_RETRIES = 5
retries = 0
while "autograding" not in sys.modules:
    try:
        import autograding
        from autograding.case import FuncCall, InOut
    except ImportError:
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
        retries += 1
    if retries >= MAX_RETRIES:
        sys.exit("[import autograding] Too many retries, exiting")


class TestNRIC(autograding.TestInputOutput):
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
