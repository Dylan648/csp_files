import tkinter as tk
import string
from passlib.hash import pbkdf2_sha256

def handle_login():
    pass

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

def encrypt_password(password):
    encrypted_pass = pbkdf2_sha256.hash(password)
    return encrypted_pass

def submit_sign_up():
    password = encrypt_password(pass_entry.get())
    if is_valid_pass(password):
        users[user_entry.get()] = password
        print('valid')
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