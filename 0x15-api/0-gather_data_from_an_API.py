#!/usr/bin/python3
"""Gets all tasks of a user."""


if __name__ == "__main__":
    from sys import argv
    import requests
    url = "https://jsonplaceholder.typicode.com"
    users_path = "/users/{}".format(argv[1])
    todos_path = "/todos?userId={}".format(argv[1])
    user = requests.get(url + users_path).json()
    todos = requests.get(url + todos_path).json()
    completed = list(filter(lambda todo: todo.get("completed"), todos))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"),
        len(completed),
        len(todos)
    ))
    for todo in completed:
        print("\t " + todo.get("title"))
