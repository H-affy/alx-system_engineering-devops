#!usr/bin/python3
"""export data in the CSV format."""

import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    user_res = requests.get(url + "users/{}".format(user_id))
    user = user_res.json()
    username = user.get("username")

    params = {"userId": user_id}
    todo_res = requests.get(url + "todos", params=params)
    todos = todo_res.json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writers = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writers.writerow(
                    [user_id, username, todo.get("completed"),
                        todo.get("title")])
