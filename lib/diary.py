class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

class DiaryEntry:
    def __init__(self, date: Date, content: str, reading_time: int):
        self.date = date
        self.content = content
        self.reading_time = reading_time

class Diary:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry: DiaryEntry):
        self.entries.append(entry)

    def read_entries(self, time_available: int, reading_speed: int):
        readable_entries = []
        for entry in self.entries:
            if entry.reading_time <= time_available:
                readable_entries.append(entry)
                time_available -= entry.reading_time
            else:
                break
        return readable_entries

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        self.tasks.append(task)

class Contact:
    def __init__(self, name: str, mobile_number: str):
        self.name = name
        self.mobile_number = mobile_number 