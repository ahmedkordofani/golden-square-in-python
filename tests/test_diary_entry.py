# test_diary_entry.py
import unittest
from lib.diary_entry import DiaryEntry

class TestDiaryEntry(unittest.TestCase):

    def test_format(self):
        entry = DiaryEntry("My Title", "These are the contents.")
        formatted_entry = entry.format()
        self.assertEqual(formatted_entry, "My Title: These are the contents.")

    def test_count_words(self):
        entry = DiaryEntry("Title", "This is a test sentence.")
        word_count = entry.count_words()
        self.assertEqual(word_count, 5)

    def test_reading_time(self):
        entry = DiaryEntry("Title", "This is a test.")
        estimated_reading_time = entry.reading_time(200)
        self.assertEqual(estimated_reading_time, 0)

    def test_reading_chunk(self):
        entry = DiaryEntry("Title", "This is a test.")
        chunk = entry.reading_chunk(200, 1)
        self.assertEqual(chunk, "This is a test.")

if __name__ == "__main__":
    unittest.main()
