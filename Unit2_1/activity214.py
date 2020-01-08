##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("300x200")
root.title('Authorization')

frame_login = tk.Frame(root)
frame_login.grid()

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

pass_lbl = tk.Label(frame_login, text='Password: ', font='Courier')
pass_lbl.pack()
ent_pass = tk.Entry(frame_login, bd=3, show='*')
ent_pass.pack(pady=5)

btn_login = tk.Button(frame_login, text="Login")
btn_login.pack(pady=5)

root.mainloop()