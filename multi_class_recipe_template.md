# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

> As a user
> So that I can record my experiences
> I want to keep a regular diary

> As a user
> So that I can reflect on my experiences 
> I want to read my past diary entries

> As a user
> So that I can reflect on my experiences in my busy day
> I want to select diary entries to read based on how much time I have and my reading speed

> As a user
> So that I can keep track of my tasks
> I want to keep a todo list along with my diary

> As a user
> So that I can keep track of my contacts
> I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

```
             +---------------------+
             |      DiaryEntry     |
             +---------------------+
             | - date: Date        |
             | - content: str      |
             | - reading_time: int |
             +---------------------+
                    |
                    |
                    ▼
             +---------------------+
             |         Diary       |
             +---------------------+
             | - entries: List[DiaryEntry]|
             | - todo_list: List[str]      |
             +---------------------+
                    |
                    |
                    ▼
             +---------------------+
             |       Contact       |
             +---------------------+
             | - name: str          |
             | - mobile_number: str |
             +---------------------+
```
## Class Interface Details:

**Diary Entry Class:**
```python
class DiaryEntry:
    def __init__(self, date: Date, content: str, reading_time: int):
        pass

class Date:
    def __init__(self, year: int, month: int, day: int):
        pass
```
**Diary Class:**

```python
class Diary:
    def __init__(self):
        pass

    def add_entry(self, entry: DiaryEntry):
        pass

    def read_entries(self, time_available: int, reading_speed: int):
        pass

class TodoList:
    def __init__(self):
        pass

    def add_task(self, task: str):
        pass

class Contact:
    def __init__(self, name: str, mobile_number: str):
        pass
```
## 3. Create Examples as Integration Tests

**Diary and TodoList Integration Test:**
```python
# EXAMPLE

"""
Given a diary and a todo list
When we add a diary entry and a task
We see those entries reflected in the diary and todo list
"""
diary = Diary()
todo_list = TodoList()
entry = DiaryEntry(Date(2023, 9, 28), "Today was a great day!", 10)
task = "Finish the project"
diary.add_entry(entry)
todo_list.add_task(task)
diary.entries  # => [entry]
todo_list.tasks  # => [task]
```
**Contact Integration Test:**
```python
# EXAMPLE

"""
Given a list of contacts
When we add a new contact
We see the new contact in the list of contacts
"""
contact_list = [Contact("Alice", "123-456-7890"), Contact("Bob", "987-654-3210")]
new_contact = Contact("Charlie", "555-555-5555")
contact_list.append(new_contact)
contact_list  # => [Alice, Bob, Charlie]
```

## 4. Create Examples as Unit Tests

**DiaryEntry Unit Test:**
```python
# EXAMPLE

"""
Given a diary entry with a date, content, and reading time
We see the date, content, and reading time reflected in the DiaryEntry properties
"""
entry = DiaryEntry(Date(2023, 9, 28), "Today was a great day!", 10)
entry.date  # => Date(2023, 9, 28)
entry.content  # => "Today was a great day!"
entry.reading_time  # => 10
```
**Diary Unit Test:**
```python
# EXAMPLE

"""
Given an empty diary
When we add a diary entry
We see the diary entry in the diary's entries
"""
diary = Diary()
entry = DiaryEntry(Date(2023, 9, 28), "Today was a great day!", 10)
diary.add_entry(entry)
diary.entries  # => [entry]
```
**TodoList Unit Test**
```python
# EXAMPLE

"""
Given an empty todo list
When we add a task
We see the task in the todo list's tasks
"""
todo_list = TodoList()
task = "Finish the project"
todo_list.add_task(task)
todo_list.tasks  # => [task]
```
**Contact Unit Test**
```python
# EXAMPLE

"""
Given a contact with a name and mobile number
We see the name and mobile number reflected in the Contact properties
"""
contact = Contact("Alice", "123-456-7890")
contact.name  # => "Alice"
contact.mobile_number  # => "123-456-7890"
```

## 5. Implement the Behaviour

**Date Class Implementation:**
```python
class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
```
**DiaryEntry Class Implemention:**
```python
class DiaryEntry:
    def __init__(self, date: Date, content: str, reading_time: int):
        self.date = date
        self.content = content
        self.reading_time = reading_time
```
**Diary Class Implementation:**
```python
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
```
**TodoList Class Implementation:**
```python
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        self.tasks.append(task)
```
**Contact Class Implementation:**
```python
class Contact:
    def __init__(self, name: str, mobile_number: str):
        self.name = name
        self.mobile_number = mobile_number 
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
