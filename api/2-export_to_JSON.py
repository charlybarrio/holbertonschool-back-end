#!/usr/bin/python3
"""using this REST API, for a given employee ID, returns TODO list"""
import json
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

    tasks = []
    for task in todos:
        tasks.append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': employee.get('username')
        })
    task_dict = {}
    task_dict[employee.get('id')] = tasks
    with open('{}.json'.format(employee.get('id')), 'w+', encoding='UTF8') as f:
        f.write(json.dumps(task_dict))

