#!/usr/bin/python3
"""Gets all tasks of a user and creates a CSV file."""


if __name__ == "__main__":
    from sys import argv
    import requests
    url = "https://jsonplaceholder.typicode.com"
    users_path = "/users/{}".format(argv[1])
    todos_path = "/todos?userId={}".format(argv[1])
    user = requests.get(url + users_path).json()
    todos = requests.get(url + todos_path).json()
    with open('{}.csv'.format(argv[1]), mode='w') as f:
        for todo in todos:
            f.write('"{}","{}","{}","{}"\n'.format(
                argv[1],
                user.get("username"),
                todo.get("completed"),
                todo.get("title")
            ))
