from lib.task_manager import TaskList


def test_TaskList():
    """
    Given an empty task list
    #add_task adds a new task to the list
    #view_tasks returns an empty list
    """
    task_list = TaskList()
    task_list.add_task("Buy groceries")
    assert task_list.view_tasks() == ["Buy groceries"]

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