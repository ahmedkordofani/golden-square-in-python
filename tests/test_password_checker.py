# File: test_password_checker.py

import unittest
from lib.password_checker import PasswordChecker

class TestPasswordChecker(unittest.TestCase):

    def test_valid_password(self):
        password_checker = PasswordChecker()
        result = password_checker.check("SecurePwd123")
        self.assertTrue(result)

    def test_invalid_short_password(self):
        password_checker = PasswordChecker()
        with self.assertRaises(Exception) as context:
            password_checker.check("Pwd123")
        self.assertEqual(str(context.exception), "Invalid password, must be 8+ characters.")

if __name__ == '__main__':
    unittest.main()
