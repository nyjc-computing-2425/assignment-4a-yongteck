import contextlib
import subprocess
import sys
import unittest

# limit number of retries
MAX_RETRIES = 5
retries = 0

# Force reload of autograding submodule
# This allows it to be updated even after students have accepted an assignment
# It would otherwise require them to delete and re-accept the assignment
# (or alternatively update the submodule manually)
def unload():
    global autograding
    if "autograding" in sys.modules:
        del sys.modules["autograding"]
    with contextlib.suppress(NameError):
        del autograding

unload()
subprocess.run(["git", "submodule", "update", "--init", "--remote"])
import autograding
from autograding.case import FuncCall, InOut


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
