tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        if not tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
    elif choice == '3':
        if not tasks:
            print("No tasks to delete.")
        else:
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
