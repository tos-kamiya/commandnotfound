import unittest
import subprocess


from commandnotfound import _print


class CommandNotFoundPrintTest(unittest.TestCase):
    def test_simple(self):
        try:
            subprocess.run(["gitk"])
        except FileNotFoundError as e:
            _print(e)
