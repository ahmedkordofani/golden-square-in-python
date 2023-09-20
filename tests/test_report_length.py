# File: test_report_length.py

import unittest
from lib.report_length import report_length

class TestReportLengthFunction(unittest.TestCase):

    def test_report_length(self):
        result = report_length("Hello, World!")
        self.assertEqual(result, "This string was 13 characters long.")

if __name__ == '__main__':
    unittest.main()
