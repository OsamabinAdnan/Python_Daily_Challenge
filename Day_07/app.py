def display_menu():
    print("\nWelcome to To-Do List!")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task Added! ✅")

def show_tasks(tasks):
    if not tasks:
        print("No tasks available! 📭")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Deleted Task: {removed_task} ❌")
            else:
                print("Invalid task number! ⚠️")
        except ValueError:
            print("Please enter a valid number! 🔢")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please select a valid option. 🚨")

if __name__ == "__main__":
    main()
