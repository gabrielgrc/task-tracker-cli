import sys
import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

# Utility function to load tasks from the JSON file
def loadTasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Utility function to save tasks to the JSON file
def saveTasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Generate a new unique ID for tasks
def generate_id(tasks):
    return max([task['id'] for task in tasks], default=0) + 1

# Command: Add a new task
def addTask(description):
    tasks = loadTasks()
    task_id = generate_id(tasks)
    now = datetime.now().isoformat()
    newTask = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }
    tasks.append(newTask)
    saveTasks(tasks)
    print(f'Task added succesfully (ID: {task_id})')

# Command: Update an existing task's description
def updateTask(task_id, description):
    tasks = loadTasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            saveTasks(tasks)
            print(f'Task {task_id} updated succesfully.')
            return
    print(f'Task {task_id} not found.')

# Command: Delete a task
def deleteTask(task_id):
    tasks = loadTasks()
    updatedTasks = [task for task in tasks if task['id'] != task_id]
    if len(updatedTasks) < len(tasks):
        saveTasks(updatedTasks)
        print(f'Task {task_id} deleted succesfully.')
    else:
        print(f'Task {task_id} not found.')

# Command: Mark a task as in-progress
def markInProgress(task_id):
    markTaskStatus(task_id, 'in-progress')

# Command: Mark a task as done
def markDone(task_id):
    markTaskStatus(task_id, 'done')

# Utility to change task status
def markTaskStatus(task_id, status):
    tasks = loadTasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            saveTasks(tasks)
            print(f'Task {task_id} marked as {status}.')
            return 
    print(f'Task {task_id} not found.')

# Command: List tasks (all, by status)
def listTasks(filterStatus=None):
    tasks = loadTasks()
    if filterStatus:
        tasks = [task for task in tasks if task['status'] == filterStatus]
    if tasks:
        for task in tasks:
            print(f"{task['id']}: {task['description']} (Status: {task['status']}, Created: {task['createdAt']}, Updated: {task['updatedAt']})")
    else:
        print("No tasks found.")

# Command-line argument parsing
def main():
    if len(sys.argv) < 2:
        print('Usage: task-cli <command> [args...]')
        return
    
    command = sys.argv[1]

    if command == 'add' and len(sys.argv) == 3:
        addTask(sys.argv[2])
    elif command == 'update' and len(sys.argv) == 4:
        updateTask(int(sys.argv[2]), sys.argv[3])
    elif command == 'delete' and len(sys.argv) == 3:
        deleteTask(int(sys.argv[2]))
    elif command == 'mark-in-progress' and len(sys.argv) == 3:
        markInProgress(int(sys.argv[2]))
    elif command == 'mark-done' and len(sys.argv) == 3:
        markDone(int(sys.argv[2]))
    elif command == 'list' and len(sys.argv) == 2:
        listTasks()
    elif command == 'list' and len(sys.argv) == 3:
        listTasks(sys.argv[2])
    else:
        print("Invalid command or arguments")

if __name__ == '__main__':
    main()