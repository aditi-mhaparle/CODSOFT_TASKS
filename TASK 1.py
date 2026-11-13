tasks = []
while True:
    print("\n To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter Task: ")
        tasks.append({"task": task, "Done": False})
        print("Task Added!")

    elif choice == "2":
        if not tasks:
            print("No Tasks Found!")
        else:
            for t in tasks:
                print(t["task"], t["Done"])

    elif choice == "3":
        if not tasks:
            print("No Tasks Found!")
        else:
            for i, t in enumerate(tasks):
                print(i + 1, t["task"])

            num = int(input("Enter the task number to update: "))

            if 1 <= num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[num - 1]["task"] = new_task
                print("Task Updated!")
            else:
                print("Invalid Task Number!")

    elif choice == "4":
        if not tasks:
            print("No Tasks Found!")
        else:
            for i, t in enumerate(tasks):
                print(i + 1, t["task"])

            num = int(input("Enter the task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task Deleted!")
            else:
                print("Invalid Task Number!")

    elif choice == "5":
        for i, t in enumerate(tasks):
            print(i + 1, t["task"])

        num = int(input("Enter the task number to completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["Done"] = True
            print("Task mark as completed!")
        else:
            print("Invalid Task Number!")

    elif choice == "6":
        print("Thank you for using To-Do Application!")
        break
