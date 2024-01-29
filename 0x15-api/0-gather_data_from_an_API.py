#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given
employee ID, returns information about his/her
TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todo", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
       users.get("name"), len(completed), len(todo)))
    [print("\t {}".format(c)) for c in completed]
