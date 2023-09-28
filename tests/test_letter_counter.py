# File: tests/test_letter_counter.py

from lib.letter_counter import LetterCounter

def test_calculate_most_common():
    counter = LetterCounter("Digital Punk")
    result = counter.calculate_most_common()
    assert result == [3, "i"]
