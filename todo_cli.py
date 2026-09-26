import json

FILENAME = "tasks.json" # Main File
tasks = []


def load_tasks():
    global tasks
    try:
        with open(FILENAME, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []


def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)


def add_task(description):
    tasks.append({"description": description, "done": False})


def show_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, start=1):
        status = "x" if task["done"] else " "
        print(f"[{status}] {i}. {task['description']}")


def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
    else:
        print("Invalid task number.")


def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        print("Invalid task number.")


def main():
    load_tasks()
    while True:
        print("\n1. Show tasks \n2. Add task \n3. Complete task \n4. Remove task \n5. Quit")
        choice = input("Choose: ")

        if choice == "1": # Show Tasks
            show_tasks()
        elif choice == "2": # Add A Task
            add_task (input("Task decription: "))
            save_tasks()
        elif choice == "3": # Completes A Task
            show_tasks()
            try:
                i = int(input("Task number to complete: ")) - 1
                complete_task(i)
                save_tasks()
            except ValueError:
                print("Please enter a number.")
        elif choice == "4": # Removes A Task
            show_tasks()
            try:
                i = int(input("Task number to remove: ")) - 1
                remove_task(i)
                save_tasks()
            except ValueError:
                print("Please enter a number.")
        elif choice == "5": # Closes file
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
