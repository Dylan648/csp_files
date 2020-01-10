import tkinter

root = tkinter.Tk()

root.geometry("800x600")
root.title("Login")

user_label = tkinter.Label(root, text='Username: ')
user_label.pack()

root.mainloop()