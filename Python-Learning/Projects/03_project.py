import requests
# Simple To-Do List App

import os

# File to save tasks
FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks yet! 🎉")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Main app loop
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter your task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added! ✅")
        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                index = int(input("Enter task number to remove: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    save_tasks(tasks)
                    print(f"Removed task: {removed} ❌")
                else:
                    print("Invalid task number!")
        elif choice == "4":
            print("Bye! 👋")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
