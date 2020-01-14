import tkinter as tk
import string

def handle_login():
    if is_valid_pass(pass_entry.get()):
        print('valid')
        error_message.config(text='')
    else:
        error_message.config(text='invalid password')

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
pass_entry = tk.Entry(root, show='*')
pass_entry.pack(pady=5)

error_message = tk.Label(root)
error_message.pack()

submit = tk.Button(root, text='Login', command=handle_login)
submit.pack()

sign_up = tk.Button(root, text='Sign Up')
sign_up.pack(pady=5)

root.mainloop()