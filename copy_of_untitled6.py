def todo_list():
    tasks = []

    while True:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks):
            print(str(i + 1) + ". " + task) 

        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added!")
        elif choice == '2':
            index_str = input("Enter the index of the task to remove: ")
            if index_str.isdigit():
                index = int(index_str) - 1
                if 0 <= index < len(tasks):
                    removed_task = tasks.pop(index)
                    print("Task '" + removed_task + "' removed!") 
                else:
                    print("Invalid index.")
            else:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

todo_list()
