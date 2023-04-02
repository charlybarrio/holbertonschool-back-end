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

    completed_tasks = [{"task": task.get(
        'title'), "completed": task.get(
            'completed'), "username": employee.get('username')}
                       for task in todos if task.get('completed') is True]

    data = {employee_id: completed_tasks}

    with open('{}.json'.format(employee_id), mode='w') as f:
        json.dump(data, f)
