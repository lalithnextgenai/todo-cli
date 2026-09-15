import json
import os

DATA_FILE = "todo.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks, description):
    tasks.append({
        "description": description,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['description']}")


def complete_task(tasks, number):
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    tasks[number - 1]["completed"] = True
    save_tasks(tasks)
    print("Task completed.")


def delete_task(tasks, number):
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    tasks.pop(number - 1)
    save_tasks(tasks)
    print("Task deleted.")


def clear_completed_tasks(tasks):
    tasks[:] = [task for task in tasks if not task["completed"]]
    save_tasks(tasks)
    print("Completed tasks cleared.")


def main():
    tasks = load_tasks()

    while True:
        print("\n MY TO-DO List")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Clear completed tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task: ").strip()

            if description:
                add_task(tasks, description)
            else:
                print("Task description cannot be empty.")

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            try:
                number = int(input("Enter task number: "))
                complete_task(tasks, number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            try:
                number = int(input("Enter task number: "))
                delete_task(tasks, number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            clear_completed_tasks(tasks)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()


