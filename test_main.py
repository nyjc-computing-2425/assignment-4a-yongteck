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
    proc = subprocess.Popen(["python", "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True)
    try:
        stdout, stderr = proc.communicate(input=input_, timeout=1)
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout, stderr = proc.communicate()
    finally:
        # Strip prompt from stdout; use colon to detect
        if stdout.strip():
            stdout = stdout[stdout.find(':') + 1:].lstrip()
        return stdout


class TestInputOutput(unittest.TestCase):

    def test_valid_t(self):
        testcase = "T0102051F\n"
        testans = "NRIC is valid.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")

    def test_valid_s(self):
        testcase = "S8521097A\n"
        testans = "NRIC is valid.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")

    def test_range_check(self):
        testcase = "C1234567C\n"
        testans = "NRIC is invalid.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")

    def test_length_check(self):
        testcase = "S123456B\n"
        testans = "NRIC is invalid.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")

    def test_checksum(self):
        testcase = "S1234567A\n"
        testans = "NRIC is invalid.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")


if __name__ == '__main__':
    unittest.main()
