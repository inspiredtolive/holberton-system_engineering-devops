#!/usr/bin/python3
"""Gets all tasks and creates a JSON file."""


if __name__ == "__main__":
    from sys import argv
    import json
    import requests
    url = "https://jsonplaceholder.typicode.com"
    users_path = "/users"
    todos_path = "/todos"
    all_tasks = {}
    users = requests.get(url + users_path).json()
    todos = requests.get(url + todos_path).json()
    for user in users:
        all_tasks[user.get("id")] = []
        for todo in todos:
            if user.get("id") == todo.get("userId"):
                all_tasks[user.get("id")].append({
                    "username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                })
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_tasks, f)
