import unittest
import subprocess


from commandnotfound import wrap


class CommandNotFoundWrapTest(unittest.TestCase):
    def test_simple(self):
        wrapped_run = wrap(subprocess.run)
        with self.assertRaises(FileNotFoundError):
            wrapped_run(["converT"])

