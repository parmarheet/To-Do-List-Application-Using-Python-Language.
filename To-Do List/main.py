tasks = ["Example Task 1", "Example Task 2"]  # Sample list of tasks

def view_tasks():
    print("Current Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task():
    new_task = input("Enter the new task: ")
    tasks.append(new_task)
    print("Task added successfully.")

def updated_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_num - 1] = new_task
                print("Task updated successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks available to update.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks available to delete.")

def display_menu():
    print("\nTo-Do List Application Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            updated_task()  # Corrected function name
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()
