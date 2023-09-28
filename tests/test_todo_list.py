# File: tests/test_todo_list.py

import unittest
from lib.todo_list import *

class TestTodoList(unittest.TestCase):
    def test_add_todo(self):
        todo_list = TodoList()
        todo1 = Todo("Task 1")
        todo2 = Todo("Task 2")

        todo_list.add(todo1)
        todo_list.add(todo2)

        self.assertEqual(len(todo_list.incomplete()), 2)

    def test_incomplete(self):
        todo_list = TodoList()
        todo1 = Todo("Task 1")
        todo2 = Todo("Task 2")

        todo_list.add(todo1)
        todo_list.add(todo2)

        incomplete_todos = todo_list.incomplete()
        self.assertEqual(len(incomplete_todos), 2)
        self.assertEqual(incomplete_todos[0].task, "Task 1")
        self.assertEqual(incomplete_todos[1].task, "Task 2")
        self.assertFalse(incomplete_todos[0].complete)
        self.assertFalse(incomplete_todos[1].complete)

    def test_complete(self):
        todo_list = TodoList()
        todo1 = Todo("Task 1")
        todo2 = Todo("Task 2")

        todo_list.add(todo1)
        todo_list.add(todo2)

        todo1.mark_complete()
        complete_todos = todo_list.complete()

        self.assertEqual(len(complete_todos), 1)
        self.assertEqual(complete_todos[0].task, "Task 1")
        self.assertTrue(complete_todos[0].complete)

    def test_give_up(self):
        todo_list = TodoList()
        todo1 = Todo("Task 1")
        todo2 = Todo("Task 2")

        todo_list.add(todo1)
        todo_list.add(todo2)

        todo_list.give_up()
        incomplete_todos = todo_list.incomplete()

        self.assertEqual(len(incomplete_todos), 0)

if __name__ == "__main__":
    unittest.main()
