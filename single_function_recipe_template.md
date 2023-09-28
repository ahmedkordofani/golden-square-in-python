# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

> As a user
> So that I can keep track of my tasks
> I want a program that I can add todo tasks to and see a list of them.

> As a user
> So that I can focus on tasks to complete
> I want to mark tasks as complete and have them disappear from the list.


## 2. Design the Class Interface


```python
class TaskList:
    def __init__(self):
        # Initialize an empty task list
        pass

    def add_task(self, task_description):
        """
        Add a new task to the task list.

        Parameters:
            task_description (str): The description of the task to be added.

        Returns:
            None

        Side Effects:
            Appends the task to the task list.
        """
        pass

    def view_tasks(self):
        """
        View the list of tasks in the task list.

        Returns:
            list of str: A list of task descriptions.
        """
        pass

    def complete_task(self, task_index):
        """
        Mark a task as complete and remove it from the task list.

        Parameters:
            task_index (int): The index of the task to be marked as complete.

        Returns:
            None

        Side Effects:
            Removes the specified task from the task list.
        """
        pass

```

## 3. Create Examples as Tests


```python
"""
Given an empty task list
#add_task adds a new task to the list
#view_tasks returns an empty list
"""
task_list = TaskList()
task_list.add_task("Buy groceries")
assert task_list.view_tasks() == []

"""
Given a task list with one task
#view_tasks returns a list with one task
#complete_task removes the task from the list
"""
task_list = TaskList()
task_list.add_task("Buy groceries")
assert task_list.view_tasks() == ["Buy groceries"]
task_list.complete_task(0)
assert task_list.view_tasks() == []

"""
Given a task list with multiple tasks
#view_tasks returns a list with all tasks in the order they were added
#complete_task removes the completed task and keeps the others
"""
task_list = TaskList()
task_list.add_task("Buy groceries")
task_list.add_task("Clean the house")
task_list.add_task("Do laundry")
assert task_list.view_tasks() == ["Buy groceries", "Clean the house", "Do laundry"]
task_list.complete_task(1)
assert task_list.view_tasks() == ["Buy groceries", "Do laundry"]

```
## 4. Implement the Behaviour



```python
class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        self.tasks.append(task_description)

    def view_tasks(self):
        return self.tasks

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
