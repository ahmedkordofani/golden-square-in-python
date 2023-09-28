# test_grammar_stats.py
import unittest  # Import the unittest module for writing and running tests
from lib.grammar_stats import GrammarStats  # Import the GrammarStats class from the lib directory

class TestGrammarStats(unittest.TestCase):  # Define a test class that inherits from unittest.TestCase

    def test_check_valid(self):
        # Test case for checking valid sentences
        grammar_checker = GrammarStats()  # Create an instance of the GrammarStats class
        self.assertTrue(grammar_checker.check("This is a valid sentence."))  # Assert that the check method returns True for a valid sentence

    def test_check_invalid(self):
        # Test case for checking invalid sentences
        grammar_checker = GrammarStats()  # Create another instance of the GrammarStats class
        self.assertFalse(grammar_checker.check("invalid sentence"))  # Assert that the check method returns False for an invalid sentence

    def test_percentage_good(self):
        # Test case for calculating the percentage of good sentences
        grammar_checker = GrammarStats()  # Create yet another instance of the GrammarStats class
        grammar_checker.check("This is a valid sentence.")  # Check a valid sentence
        grammar_checker.check("invalid sentence")  # Check an invalid sentence
        percentage = grammar_checker.percentage_good()  # Calculate the percentage of good sentences
        self.assertEqual(percentage, 50.0)  # Assert that the calculated percentage matches the expected value

if __name__ == "__main__":
    unittest.main()  # Run the unittest framework if this script is executed directly
