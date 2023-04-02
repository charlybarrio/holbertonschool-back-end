#!/usr/bin/python3
"""extend your Python script to export data in the CSV format"""
import csv
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

    filename = '{}.csv'.format(employee_id)

    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                    [employee_id, employee['username'], task['completed']
                        task['title']])

    print("Employee {} is done with tasks({}/{}):".format(employee.get('name'),
          len([t for t in todos if t['completed']]), len(todos)))
