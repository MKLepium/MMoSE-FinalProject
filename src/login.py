# -*- coding: utf-8 -*-
#from __future__ import print_function, unicode_literals
#from PyInquirer import prompt, print_json
from src import user_database

#username_prompt = [
#    {
#        'type': 'input',
#        'name': 'username',
#        'message': 'Insert Username',
#    }
#]
#password_prompt = [
#    {
#        'type': 'input',
#        'name': 'password',
#        'message': 'Insert Password',
#    }
#]

def login():
    user = start()
    if user == "Username not found":
        print("Username not found")
        return login()
    if user == "Password not correct":
        print("Password not correct")
        return login()
    return user

def start():
    #answers = prompt(username_prompt)
    #username = answers["username"]
    #answers2 = prompt(password_prompt)
    #password = answers2["password"]
    username = input("Insert Username: ")
    password = input("Insert Password: ")

    user = user_database.find_user(username)
    if user == None:
        return "Username not found"
    if user.password != password:
        return "Password not correct"
    return user
    
            

