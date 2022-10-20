# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from src import user_database

username_prompt = [
    {
        'type': 'input',
        'name': 'username',
        'message': 'Insert Username',
    }
]
password_prompt = [
    {
        'type': 'input',
        'name': 'password',
        'message': 'Insert Password',
    }
]

def start():
    answers = prompt(username_prompt)
    username = answers["username"]
    answers2 = prompt(password_prompt)
    password = answers2["password"]
    
    user = next((x for x in user_database.users if x.name == username), None)
    if user == None:
        print("Username not found")
        start() # User not found
    if user.password != password:
        print("Wrong Password")
        start()
    return user
    
            

