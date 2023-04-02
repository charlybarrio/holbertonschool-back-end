#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests


if __name__ == "__main__":

    users_url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(users_url).json()

    all_tasks = {}
    for user in users:
        todos_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(user['id']))
        todos = requests.get(todos_url).json()
        tasks = []
        for todo in todos:
            task = {'username': user['username'], 'task': todo['title'],
                    'completed': todo['completed']}
            tasks.append(task)
        all_tasks[user['id']] = tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f)
