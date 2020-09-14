#!/usr/bin/python3
"""
Gets information about Employees and saves to JSON DERULO
"""
import json
import requests


if __name__ == "__main__":
    local = 'https://jsonplaceholder.typicode.com/'
    all_info = {}
    user_id = 1
    while user_id < 11:
        el_user = requests.get(local + 'users/{}'.format(user_id))
        el_user = el_user.json()
        name = el_user.get('username')
        req = requests.get(
            local + 'todos?' + 'userId={}'.format(str(user_id)))
        content = req.json()
        all_info[str(user_id)] = []
        for item in content:
            thingy = {"username": name,
                      "task": item.get('task'),
                      "completed": item.get('completed')}
            all_info.get(str(user_id)).append(thingy)
        user_id += 1
    with open('todo_all_employees.json', 'w') as new_buf:
        all_info = json.dumps(all_info)
        new_buf.write(all_info)
        new_buf.close()
