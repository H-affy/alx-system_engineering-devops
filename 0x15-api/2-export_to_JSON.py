#!/usr/bin/python3
"""script to export data in the JSON format."""

import requests
import sys
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    params = {"userId": user_id}
    todos = requests.get(url + "todos", params=params).json()
    data_export = {user_id: []}
    for todo in todos:
        task_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "user_name": username
                }
        data_export[user_id].append(task_info)

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_export, jsonfile, indent=4)
