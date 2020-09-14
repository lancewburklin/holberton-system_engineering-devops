#!/usr/bin/python3
"""
Gets information about Employees and saves to CSV
"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        completed = 0
        local = 'https://jsonplaceholder.typicode.com/'
        name = requests.get(local + 'users/{}'.format(sys.argv[1]))
        name = name.json()
        name = name.get('username')
        req = requests.get(
            local + 'todos?' + 'userId={}'.format(sys.argv[1]))
        content = req.json()
        with open(sys.argv[1] + ".csv", 'w') as new_buf:
            writer = csv.writer(new_buf, quoting=csv.QUOTE_ALL)
            for things in content:
                stuff = [str(sys.argv[1]), str(name),
                         str(things.get('completed')),
                         str(things.get('title'))]
                writer.writerow(stuff)
            new_buf.close()
