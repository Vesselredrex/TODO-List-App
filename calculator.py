import os
import json

TODO_FiLE = 'todo_list.json'

def load_todo_list():
    if os.path.exists(TODO_FiLE):
        with open(TODO_FiLE, 'r') as file:
            return json.load(file)
    return [] 

def save_todo_list(todo_list):
    with open(TODO_FiLE, 'w') as file:
        json.dump(todo_list, file)

def add_task(todo_list, task):
   task_id = str(len(todo_list) + 1)
   todo_list(task_id) = task
   save_todo_list(todo_list)
   print(f"Task added with ID: {task_id}")

def delete_task