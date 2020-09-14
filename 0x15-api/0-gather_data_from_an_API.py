#!/usr/bin/python3
"""
Gets information about an employee's to-do list
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        completed = 0
        local = 'https://jsonplaceholder.typicode.com/'
        name = requests.get(local + 'users/{}'.format(sys.argv[1]))
        name = name.json()
        req = requests.get(
            local + 'todos?' + 'userId={}'.format(sys.argv[1]))
        content = req.json()
        for things in content:
            if things.get('completed') is True:
                completed += 1
        print("Employee {} is done with tasks({}/20)".format(
            name.get('name'), str(completed)))
        for task in content:
            if task.get('completed') is True:
                print('\t ' + task.get('title'))
