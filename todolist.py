class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task_desc = input("Enter task description: ")
        task = {
            "description": task_desc,
            "completed": False
        }
        self.tasks.append(task)
        print(" Task added successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available here.\n")
            return

        print("\n--- To-Do List ---")
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['description']} - {status}")
        print()

    def mark_completed(self):
        self.view_tasks()
        if not self.tasks:
            return

        try:
            task_no = int(input("Enter task number to mark as completed: "))
            if 1 <= task_no <= len(self.tasks):
                self.tasks[task_no - 1]["completed"] = True
                print(" Task marked as completed!\n")
            else:
                print("Invalid task number please check again.\n")
        except ValueError:
            print(" Please enter a valid number.\n")


# -------- Main Program --------
todo = TodoList()

while True:
    print("===== To-Do List Application =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        todo.add_task()
    elif choice == "2":
        todo.view_tasks()
    elif choice == "3":
        todo.mark_completed()
    elif choice == "4":
        print("Thank you for using To-Do List Application")
        break
    else:
        print("Invalid choice. Try again.\n")

