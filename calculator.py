import os
import json

TODO_FILE = 'todo_list.json'

def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_todo_list(todo_list):
    with open(TODO_FILE, 'w') as file: 
        json.dump(todo_list, file)

def add_task(todo_list, task):
   task_id = str(len(todo_list) + 1)
   todo_list[task_id] = task
   save_todo_list(todo_list)
   print(f"Task added with ID: {task_id}")

def delete_task(todo_list, task_id):
    if task_id in todo_list:
        removed = todo_list.pop(task_id)
        save_todo_list(todo_list)
        print(f"Task deleted: [{task_id}] {removed}")
    else:
        print(f"No task found with ID: {task_id}")
def main():
    todo_list = load_todo_list()
    while True:
        print("\nTo-Do List Manager")
        for id, task in todo_list.items():
            print(f"[{id}] {task}")
        print("\nOptions: (1) Add Task (2) Delete Task (3) Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == '2':
            task_id = input("Enter the task ID to delete: ")
            delete_task(todo_list, task_id)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")
        
if __name__ == "__main__":
    main()