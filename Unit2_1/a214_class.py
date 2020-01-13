import tkinter as tk
import string


def handle_login():
    if len(pass_entry.get()) < 8:
        error_message.config(text='Please enter at least 8 characters')
    else:
        if not any(char.isdigit() for char in pass_entry.get()):
            error_message.config(text='Please enter at least one number')
        elif not any(char.isupper() for char in pass_entry.get()):
            error_message.config(text='Please enter at least one uppercase letter')
        elif not any(char.islower() for char in pass_entry.get()):
            error_message.config(text='Please enter at least lowercase letter')
        elif not any(char in string.punctuation for char in pass_entry.get()):
            error_message.config(text='Please enter at least one special character')    
        else:
            print('User: ',user_entry.get(), '\nPass: ', pass_entry.get())
            error_message.config(text='')

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

root.mainloop()