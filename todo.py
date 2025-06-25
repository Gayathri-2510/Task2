TASK_FILE = 'tasks.txt'

def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def view_tasks(tasks):
    if not tasks:
        print("\nto-do list is empty.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter a new task:").strip()
    if task:
        tasks.append(task)
        print(f'"{task}" has been added.')
        save_tasks(tasks)
    else:
        print("Cannot add an empty task.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
            task_num = int(input("Enter the task number to remove:"))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f'"{removed}" has been removed.')
                save_tasks(tasks)
            else:
                print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Choose an option (1-4):").strip()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("End")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()