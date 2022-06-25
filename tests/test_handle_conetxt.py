import unittest
import subprocess


from commandnotfound import handler


class CommandNotFoundHandlerTest(unittest.TestCase):
    def test_simple(self):
        with self.assertRaises(SystemExit):
            with handler():
                subprocess.run(["converT"])

