tasks = []

def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available, please add some tasks first.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete, please add some tasks first.")
    else:
        view_tasks(tasks)
        try:
            task_num = int(input("Enter the task number you want to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfuly.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


while True:
    user = input("\nGood morning user, choose the following options:\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit menu\n")

    if user == "1":
        add_task(tasks)
    elif user == "2":
        view_tasks(tasks)
    elif user == "3":
        delete_task(tasks)
    elif user == "4":
        print("Exiting the menu, take care!")
        break
    else:
        print("Invalid option, please choose a valid option.")