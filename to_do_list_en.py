task_list = []

while True:
    print("\n ======== To Do List =========")
    print("1 - Add Tasks")
    print("2 - List Tasks")
    print("3 - Remove Tasks")
    print("4 - Exit")

    menu_option = input("Select the desired option: ").strip()

    if menu_option == "1":
        added_task = input("Write the task to add to your list: ")
        task_list.append(added_task)

    elif menu_option == "2":
        if len(task_list) == 0:
            print("No tasks registered.") 
        else:
            for i, task in enumerate(task_list, start=1): 
                print(f"{i}. {task}")

    elif menu_option == "3":
        removed_task = input("Enter the task you want to remove: ")

        if removed_task in task_list:
            task_list.remove(removed_task)
            print("Task removed successfully!")
        else:
            print("Invalid task. This task is not in the list.")

    elif menu_option == "4":
        print("Exiting the program")
        break

    else:
        print("Invalid option.")