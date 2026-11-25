
class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description


FILE_NAME = "tasks.txt"
tasks = []


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) == 3:
                    task = Task(int(parts[0]), parts[1], parts[2])
                    tasks.append(task)

        print("Tasks loaded successfully!")

    except FileNotFoundError:
        print("No previous task file found. Starting fresh.")

    except (ValueError, OSError) as error:
        print("Error loading tasks:", error)


def save_tasks():
    try:
        with open(FILE_NAME, "w") as file:
            for task in tasks:
                file.write(
                    f"{task.task_id}|{task.title}|{task.description}\n"
                )

    except OSError as error:
        print("Error saving tasks:", error)


def create_task():
    task_id = max((task.task_id for task in tasks), default=0) + 1

    title = input("Enter task title: ")
    description = input("Enter task description: ")

    tasks.append(Task(task_id, title, description))
    save_tasks()

    print("Task created successfully!")


def read_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n======= TASK LIST =======")

    for task in tasks:
        print("ID:", task.task_id)
        print("Title:", task.title)
        print("Description:", task.description)
        print("-------------------------")


def update_task():
    read_tasks()

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to update: "))

        for task in tasks:
            if task.task_id == task_id:
                task.title = input("Enter new title: ")
                task.description = input("Enter new description: ")
                save_tasks()
                print("Task updated successfully!")
                return

        print("Task not found!")

    except ValueError:
        print("Please enter a valid task ID.")


def delete_task():
    read_tasks()

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task.task_id == task_id:
                tasks.remove(task)
                save_tasks()
                print("Task deleted successfully!")
                return

        print("Task not found!")

    except ValueError:
        print("Please enter a valid task ID.")


load_tasks()

while True:
    print("\n===== TASK MANAGER =====")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_task()
    elif choice == "2":
        read_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank you for using Task Manager!")
        break
    else:
        print("Invalid choice!")
