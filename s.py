tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def remove_task(index):
    try:
        del tasks[index]
        print("Task removed successfully!")
    except IndexError:
        print("Invalid task index!")

def display_tasks():
    if tasks:
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks.")

# Main function to interact with user
def main():
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            if tasks:
                display_tasks()
                index = int(input("Enter the task number to remove: ")) - 1
                remove_task(index)
            else:
                print("No tasks to remove.")
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
