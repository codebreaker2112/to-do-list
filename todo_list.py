import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    print("Tasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}")

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def update_task(tasks):
    task_id = int(input("Enter the task ID to update: "))

    for task in tasks:
        if task['id'] == task_id:
            title = input("Enter the new task title: ")
            description = input("Enter the new task description: ")
            task['title'] = title
            task['description'] = description
            save_tasks(tasks)
            print("Task updated successfully.")
            return

    print("Task not found.")

def delete_task(tasks):
    task_id = int(input("Enter the task ID to delete: "))

    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully.")
            return

    print("Task not found.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
