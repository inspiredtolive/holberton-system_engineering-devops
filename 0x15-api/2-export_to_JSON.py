#!/usr/bin/python3
"""Gets all tasks of a user and creates a JSON file."""


if __name__ == "__main__":
    from sys import argv
    import json
    import requests
    url = "https://jsonplaceholder.typicode.com"
    users_path = "/users/{}".format(argv[1])
    todos_path = "/todos?userId={}".format(argv[1])
    user = requests.get(url + users_path).json()
    todos = requests.get(url + todos_path).json()
    tasks = list(map(lambda todo: {
        "task": todo.get("title"),
        "completed": todo.get("completed"),
        "username": user.get("username")
    }, todos))
    with open('{}.json'.format(argv[1]), mode='w') as f:
        json.dump({"{}".format(argv[1]): tasks}, f)
