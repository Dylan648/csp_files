import tkinter as tk
import string
from passlib.hash import pbkdf2_sha256

def handle_login():
    user = user_entry.get()
    if user in users:
        if pbkdf2_sha256.verify(pass_entry.get(), users[user]):
            error_message.config(text='You have logged in')
        else:
            error_message.config(text='invalid password')
    else:
        error_message.config(text='User does not exist, please sign up')

def is_valid_pass(password):
    if len(password) < 8:
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.islower() for char in password):
        return False
    elif not any(char in string.punctuation for char in password):
        return False    
    return True    

def submit_sign_up():
    user = user_entry.get()
    if user in users:
        error_message.config(text='User already exists, please sign in or input a different user name')
    else:
        password = pass_entry.get()
        if is_valid_pass(password):
            hashed_password = pbkdf2_sha256.hash(password)
            users[user_entry.get()] = hashed_password
            print('valid')
            print(users)
            error_message.config(text='')
        else:
            error_message.config(text='invalid password')

users = {}
root = tk.Tk()

root.geometry("800x600")
root.title("Authorization")

instructions = tk.Label(root, text='Password should have one uppercase, lowercase, special character, and digit')
instructions.pack(pady=5)

user_label = tk.Label(root, text='Username:')
user_label.pack()
user_entry = tk.Entry(root)
user_entry.pack(pady=5)

pass_label = tk.Label(root, text='Password:')
pass_label.pack()
pass_entry = tk.Entry(root, show='')
pass_entry.pack(pady=5)

error_message = tk.Label(root)
error_message.pack()

submit = tk.Button(root, text='Login', command=handle_login)
submit.pack()

sign_up = tk.Button(root, text='Sign Up', command=submit_sign_up)
sign_up.pack(pady=5)

root.mainloop()