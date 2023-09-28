# grammar_stats.py

# Define a class called GrammarStats
class GrammarStats:
    # Constructor method: Initializes the object with two instance variables
    def __init__(self):
        # Initialize the total_checked variable to keep track of the total number of text checks
        self.total_checked = 0
        # Initialize the passed_checks variable to keep track of the number of text checks that passed
        self.passed_checks = 0
    # Method to check if a given text meets certain criteria
    def check(self, text):
        # Increment the total_checked counter each time the check method is called
        self.total_checked += 1
        # Check if the text is not empty, starts with an uppercase letter, and ends with certain punctuation
        if text and text[0].isupper() and text[-1] in ".!?":
            # If the criteria are met, increment the passed_checks counter
            self.passed_checks += 1
            # Return True to indicate that the text passed the check
            return True
        # If the criteria are not met, return False to indicate that the text did not pass the check
        return False

    # Method to calculate the percentage of texts that passed the check
    def percentage_good(self):
        # Check if no texts have been checked to avoid division by zero
        if self.total_checked == 0:
            return 0
        # Calculate the percentage of texts that passed and return the result
        return (self.passed_checks / self.total_checked) * 100
