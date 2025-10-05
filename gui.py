import tkinter as tk
from tkinter import messagebox

login = []

def Registration():
    username = reg_user_var.get().strip()
    password = reg_pass_var.get().strip()
    if not username or not password:
        messagebox.showwarning("Validation", "Username and password are required.")
        return
    for r in login:
        if r["Name"] == username:
            messagebox.showerror("Error", "Username already exists.")
            return
    record = {"Name": username, "pass": password}
    login.append(record)
    reg_user_var.set("")
    reg_pass_var.set("")
    messagebox.showinfo("Success", "Account Registered Successfully.")

def Login():
    user = login_user_var.get().strip()
    pas = login_pass_var.get().strip()
    if not user or not pas:
        messagebox.showwarning("Validation", "Username and password are required.")
        return
    isFound = False
    for i in login:
        if user == i["Name"] and pas == i["pass"]:
            isFound = True
            messagebox.showinfo("Success", "Logged in successfully.")
            break
    if not isFound:
        messagebox.showerror("Error", "Username or password incorrect.")

# Build GUI
root = tk.Tk()
root.title("Login System GUI")
root.geometry("360x240")
root.resizable(False, False)

# Frames
menu_frame = tk.Frame(root)
reg_frame = tk.Frame(root)
login_frame = tk.Frame(root)
for f in (menu_frame, reg_frame, login_frame):
    f.grid(row=0, column=0, sticky="nsew")

def show_frame(frame):
    frame.tkraise()

tk.Label(menu_frame, text="Login System", font=("Segoe UI", 14)).pack(pady=12)
tk.Button(menu_frame, text="Register", width=20, command=lambda: show_frame(reg_frame)).pack(pady=6)
tk.Button(menu_frame, text="Login", width=20, command=lambda: show_frame(login_frame)).pack(pady=6)
tk.Button(menu_frame, text="Exit", width=20, command=root.destroy).pack(pady=6)

tk.Label(reg_frame, text="Registration", font=("Segoe UI", 12)).pack(pady=8)
frm_reg = tk.Frame(reg_frame)
frm_reg.pack(pady=4)
tk.Label(frm_reg, text="Username:", width=10, anchor="w").grid(row=0, column=0, padx=4, pady=4)
reg_user_var = tk.StringVar()
tk.Entry(frm_reg, textvariable=reg_user_var, width=22).grid(row=0, column=1, padx=4, pady=4)
tk.Label(frm_reg, text="Password:", width=10, anchor="w").grid(row=1, column=0, padx=4, pady=4)
reg_pass_var = tk.StringVar()
tk.Entry(frm_reg, textvariable=reg_pass_var, width=22, show="*").grid(row=1, column=1, padx=4, pady=4)
tk.Button(reg_frame, text="Register", width=15, command=Registration).pack(pady=6)
tk.Button(reg_frame, text="Back", width=15, command=lambda: show_frame(menu_frame)).pack()

tk.Label(login_frame, text="Login", font=("Segoe UI", 12)).pack(pady=8)
frm_login = tk.Frame(login_frame)
frm_login.pack(pady=4)
tk.Label(frm_login, text="Username:", width=10, anchor="w").grid(row=0, column=0, padx=4, pady=4)
login_user_var = tk.StringVar()
tk.Entry(frm_login, textvariable=login_user_var, width=22).grid(row=0, column=1, padx=4, pady=4)
tk.Label(frm_login, text="Password:", width=10, anchor="w").grid(row=1, column=0, padx=4, pady=4)
login_pass_var = tk.StringVar()
tk.Entry(frm_login, textvariable=login_pass_var, width=22, show="*").grid(row=1, column=1, padx=4, pady=4)
tk.Button(login_frame, text="Login", width=15, command=Login).pack(pady=6)
tk.Button(login_frame, text="Back", width=15, command=lambda: show_frame(menu_frame)).pack()

show_frame(menu_frame)
root.mainloop()