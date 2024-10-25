# Task Tracker CLI

Task Tracker CLI is a command-line application for managing tasks, designed to help you keep track of your to-do list. This CLI app allows you to add, update, delete, and track tasks by status (e.g., `todo`, `in-progress`, `done`). Task data is stored in a JSON file, making it easily accessible and modifiable.

## Project URL
[Task Tracker CLI Project URL](https://github.com/gabrielgrc/task-tracker-cli)

## Features
- **Add tasks** with unique IDs and descriptions.
- **Update tasks** with new descriptions.
- **Delete tasks** by ID.
- **Change status** of tasks to `in-progress` or `done`.
- **List tasks** by overall list or filter by status (`todo`, `in-progress`, `done`).
  
## Getting Started

### Prerequisites
- Python 3.x installed on your system.
  
### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/gabrielgrc/task-tracker-cli
   ```

2. Change to the project directory:
   ```bash
   cd task-tracker-cli
   ```

### Usage
The CLI accepts various commands to manage tasks. Below are examples of how to use each command:

1. Add a new task:
   ```bash
   python task_cli.py add "Buy groceries"
   ```

2. Update a task description:
   ```bash
   python task_cli.py update <task_id> "Updated task description"
   ```

3. Delete a task:
   ```bash
   python task_cli.py delete <task_id>
   ```

4. Mark a task as in-progress:
   ```bash
   python task_cli.py mark-in-progress <task_id>
   ```

5. Mark a task as done:
   ```bash
   python task_cli.py mark-done <task_id>
   ```

6. List all tasks:
   ```bash
   python task_cli.py list
   ```

7. List tasks by status:
   ```bash
   python task_cli.py list done
   python task_cli.py list todo
   python task_cli.py list in-progress
   ```

### Example
Here's an example of adding, updating, and listing tasks:
  ```bash
  # Adding a task
  python task_cli.py add "Buy groceries"
  # Output: Task added successfully (ID: 1)
  
  # Marking it as in-progress
  python task_cli.py mark-in-progress 1
  
  # Listing all tasks
  python task_cli.py list
  ```

### Project Structure
. **task_cli.py**: Main script with CLI commands for task management.

. **tasks.json**: JSON file where all tasks are stored.

### Contributing
Feel free to fork the project and submit pull requests. For major changes, please open an issue first to discuss what you'd like to change.
