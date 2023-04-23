#to do list

# This program creates a simple todo list
#upon running this program you will be given 4 options
# 1 - Add Task, 2 - Remove Task, 3 - View Tasks (this will be updated if you just added or removed a task), 4 quit
#add your task here
tasks = []
#task is added to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
#task is removed
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")
# tasks will be viewed
def view_tasks():
    if tasks:
        print("Todo List:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("Todo List is empty.")

while True:
    print("\nChoose an option:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Quit")

    choice = input("Enter choice number: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task: ")
        remove_task(task)
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")