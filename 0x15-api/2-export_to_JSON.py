#!/usr/bin/python3
"""
Gets information about Employees and saves to JSON DERULO
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        local = 'https://jsonplaceholder.typicode.com/'
        name = requests.get(local + 'users/{}'.format(sys.argv[1]))
        name = name.json()
        name = name.get('username')
        req = requests.get(
            local + 'todos?' + 'userId={}'.format(sys.argv[1]))
        content = req.json()
        info = {str(sys.argv[1]): []}
        for item in content:
            thingy = {"task": item.get('title'),
                      "completed": item.get('completed'),
                      "username": name}
            info.get(str(sys.argv[1])).append(thingy)
        with open(sys.argv[1] + ".json", 'w') as new_buf:
            info = json.dumps(info)
            new_buf.write(info)
            new_buf.close()
