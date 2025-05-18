import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    # Load tasks from the file
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    # Save tasks to the file
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    # Add a new task
    description = input("Enter task description: ").strip()
    due_date = input("Enter due date (optional, press Enter to skip): ").strip()
    task = {
        "description": description,
        "due_date": due_date if due_date else "No due date",
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    save_tasks(tasks)

def view_tasks(tasks):
    # View all tasks
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. {task['description']} (Due: {task['due_date']}) - {status}")

def mark_task_complete(tasks):
    # Mark a task as complete
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            print("Task marked as complete!")
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input! Please enter a number.")

def edit_task(tasks):
    # Edit a task
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to edit: ")) - 1
        if 0 <= task_num < len(tasks):
            new_description = input("Enter new description (press Enter to keep current): ").strip()
            new_due_date = input("Enter new due date (press Enter to keep current): ").strip()
            if new_description:
                tasks[task_num]["description"] = new_description
            if new_due_date:
                tasks[task_num]["due_date"] = new_due_date
            print("Task updated successfully!")
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input! Please enter a number.")

def delete_task(tasks):
    # Delete a task
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            print("Task deleted successfully!")
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input! Please enter a number.")

def main():
    print("Welcome to the To-Do List Application!")
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Thank you for using the To-Do List Application. Have a Great day!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()