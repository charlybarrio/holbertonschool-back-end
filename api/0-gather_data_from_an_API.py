#!/usr/bin/python3
"""using this REST API, for a given employee ID, returns TODO list"""
import requests
from sys import argv


if __name__ == "__main__":

    employee_id = argv[1]
    user_url = ('https://jsonplaceholder.typicode.com/users/{}'
                .format(employee_id))
    employee = requests.get(user_url).json()

    todos_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
                 .format(employee_id))
    todos = requests.get(todos_url).json()

    completed_tasks = [task.get('title') for task in todos
                       if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(employee.get('name'),
          len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task))
