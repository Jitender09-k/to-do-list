# To-Do List Application

# Initialize the to-do list
todo_list = []

def add_task(task):
    """Add a task to the to-do list function."""
    todo_list.append({"task": task, "completed": False})
    print(f'Task "{task}" added to the list.')

def display_tasks():
    """Function for Display all tasks in the to-do list."""
    if not todo_list:
        print("No tasks in the to-do list.")
        return
    print("\nTo-Do List:")
    for index, task in enumerate(todo_list):
        status = "✓" if task["completed"] else "✗"
        print(f"{index + 1}. {task['task']} [{status}]")
    print() 

def remove_task(identifier):
    """Function for Remove a task from the to-do list by name or index."""
    if isinstance(identifier, int):
        if 0 < identifier <= len(todo_list):
            removed_task = todo_list.pop(identifier - 1)
            print(f'Task "{removed_task["task"]}" removed from the list.')
        else:
            print("Invalid task number.")
    else:
        for i, task in enumerate(todo_list):
            if task["task"].lower() == identifier.lower():
                removed_task = todo_list.pop(i)
                print(f'Task "{removed_task["task"]}" removed from the list.')
                return
        print(f'Task "{identifier}" not found in the list.')

def mark_task(index, status):
    """Function for Mark a task as completed or pending."""
    if 0 < index <= len(todo_list):
        todo_list[index - 1]["completed"] = status
        status_text = "completed" if status else "pending"
        print(f'Task "{todo_list[index - 1]["task"]}" marked as {status_text}.')
    else:
        print("Invalid task number.")

def main():
    """Main function to run the To-Do List application."""
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Remove Task by Name")
        print("4. Remove Task by Index")
        print("5. Mark Task as Completed")
        print("6. Mark Task as Pending")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            task_name = input("Enter the name of the task to remove: ")
            remove_task(task_name)
        elif choice == '4':
            task_index = int(input("Enter the index of the task to remove: "))
            remove_task(task_index)
        elif choice == '5':
            task_index = int(input("Enter the index of the task to mark as completed: "))
            mark_task(task_index, True)
        elif choice == '6':
            task_index = int(input("Enter the index of the task to mark as pending: "))
            mark_task(task_index, False)
        elif choice == '7':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
