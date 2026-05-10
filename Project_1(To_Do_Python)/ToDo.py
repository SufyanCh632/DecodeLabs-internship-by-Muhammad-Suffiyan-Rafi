import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Show menu
def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("⚠ No tasks available.")
        return
    
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

# Add task
def add_task(tasks):
    task_name = input("Enter task: ")
    tasks.append({"task": task_name, "completed": False})
    save_tasks(tasks)
    print("✅ Task added!")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"❌ Deleted: {removed['task']}")
    except (IndexError, ValueError):
        print("⚠ Invalid input!")

# Mark complete
def mark_complete(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("✔️ Task marked as complete!")
    except (IndexError, ValueError):
        print("⚠ Invalid input!")

# Main program
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()