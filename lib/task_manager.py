class TaskList:
    def __init__(self):
        # Initialize an empty task list
        self.tasks = []

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
        self.tasks.append(task_description)

    def view_tasks(self):
        """
        View the list of tasks in the task list.

        Returns:
            list of str: A list of task descriptions.
        """
        return self.tasks

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
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]