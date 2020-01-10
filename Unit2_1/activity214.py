##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

def test_my_button():
    frame_auth.tkraise()
    password = ent_pass.get()
    show_pass.config(text=password, font='Arial')

# main window
root = tk.Tk()
root.wm_geometry("300x200")
root.title('Authorization')

frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

pass_lbl = tk.Label(frame_login, text='Password: ', font='Courier')
pass_lbl.pack()
ent_pass = tk.Entry(frame_login, bd=3, show='*')
ent_pass.pack(pady=5)

btn_login = tk.Button(frame_login, text="Login", command=test_my_button)
btn_login.pack(pady=5)

frame_auth = tk.Frame(root)

frame_auth.grid(row=0, column=0, sticky="news")
show_pass = tk.Label(frame_auth, text='sup chief')
show_pass.pack()

frame_login.tkraise()
root.mainloop()