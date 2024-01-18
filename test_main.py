import subprocess
import unittest


def strip_prompt(stdout: str) -> str:
    """Strip the prompt from stdout.
    The prompt is assumed to end with a colon (:), followed by zero or more
    whitespace characters.
    """
    if stdout.strip():
        stdout = stdout[stdout.find(':') + 1:].lstrip()
    return stdout


def invoke_main(input_: str) -> str:
    """Invoke main.py and return its output."""
    result: subprocess.CompletedProcess = subprocess.run(
        ["python", "main.py"],
        input=input_,
        capture_output=True,
        text=True,
        timeout=3,
    )
    stdout = result.stdout
    if not stdout or stdout.strip():
        return ""
    return strip_prompt(stdout) if ":" in stdout else stdout


class TestInputOutput(unittest.TestCase):

    def check_result(self, result: str, answer: str):
        """Test the user's answer against the expected answer."""
        if answer != "":
            self.assertNotEqual(result.strip(), "", msg=f"No output from program.")
        self.assertIn(result,
          answer,
          msg=f"User output {result!r} != expected output {answer!r}")

    def test_valid_t(self):
        testcase = "T0102051F\n"
        testans = "NRIC is valid.\n"
        userans = invoke_main(testcase)
        self.test_result(userans, testans)        

    def test_valid_s(self):
        testcase = "S8521097A\n"
        testans = "NRIC is valid.\n"
        userans = invoke_main(testcase)
        self.test_result(userans, testans)        

    def test_range_check(self):
        testcase = "C1234567C\n"
        testans = "NRIC is invalid.\n"
        userans = invoke_main(testcase)
        self.test_result(userans, testans)        

    def test_length_check(self):
        testcase = "S123456B\n"
        testans = "NRIC is invalid.\n"
        userans = invoke_main(testcase)
        self.test_result(userans, testans)        

    def test_checksum(self):
        testcase = "S1234567A\n"
        testans = "NRIC is invalid.\n"
        userans = invoke_main(testcase)
        self.test_result(userans, testans)        


if __name__ == '__main__':
    unittest.main()
