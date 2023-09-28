# diary_entry.py

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words = contents.split()
        self.index = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.words)

    def reading_time(self, wpm):
        return len(self.words) // wpm

    def reading_chunk(self, wpm, minutes):
        words_to_read = wpm * minutes
        chunk = ' '.join(self.words[self.index:self.index+words_to_read])
        self.index += words_to_read
        if self.index >= len(self.words):
            self.index = 0  # Reset the index if we've read the entire contents
        return chunk
