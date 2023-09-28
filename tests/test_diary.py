from lib.diary import *


def test_date_properties():
    date = Date(2023, 9, 28)
    assert date.year == 2023
    assert date.month == 9
    assert date.day == 28

def test_diary_entry_properties():
    entry = DiaryEntry(Date(2023, 9, 28), "Today was a great day!", 10)
    assert entry.date.year == 2023
    assert entry.content == "Today was a great day!"
    assert entry.reading_time == 10

def test_diary_add_entry():
    diary = Diary()
    entry = DiaryEntry(Date(2023, 9, 28), "Today was a great day!", 10)
    diary.add_entry(entry)
    assert len(diary.entries) == 1

def test_todo_list_add_task():
    todo_list = TodoList()
    task = "Finish the project"
    todo_list.add_task(task)
    assert len(todo_list.tasks) == 1

def test_contact_properties():
    contact = Contact("Alice", "123-456-7890")
    assert contact.name == "Alice"
    assert contact.mobile_number == "123-456-7890"
