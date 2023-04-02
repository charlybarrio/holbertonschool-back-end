#!/usr/bin/python3
"""export data in the JSON format"""
import json
from sys import argv
import requests


if __name__ == "__main__":

    employee_id = argv[1]
    user_url = ('https://jsonplaceholder.typicode.com/users/{}'
                .format(employee_id))
    employee = requests.get(user_url).json()

    todos_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
                 .format(employee_id))
    todos = requests.get(todos_url).json()

    tasks = []
    for t in todos:
        tasks.append({'task': t['title'],
                      'completed': t['completed'],
                      'username': employee['username']})
    task_dict = {}
    task_dict[employee['username']] = tasks
    with open(
            '{}.json'.format(employee['username']),
            'w+', encoding='UTF8') as f:
        f.write(json.dumps(task_dict))
