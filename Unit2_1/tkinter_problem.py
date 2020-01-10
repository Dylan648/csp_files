import tkinter as tk

def handle_button_press():
    print(ent_username.get())
    print(ent_pass.get())

root = tk.Tk()
root.geometry("200x150")

lbl_username = tk.Label(root, text='Username:')
lbl_username.pack()
ent_username = tk.Entry(root, bd=3)
ent_username.pack(pady=5)

pass_lbl = tk.Label(root, text='Password: ', font='Courier')
pass_lbl.pack()
ent_pass = tk.Entry(root, bd=3, show='*')
ent_pass.pack(pady=5)

btn_login = tk.Button(root, text="Login", command=handle_button_press)
btn_login.pack(pady=5)

root.mainloop()