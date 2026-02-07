import json
import tkinter as tk

from canvas import app
from helpers import clean_screen
from products import render_products_screen

def login(username, password):
    with open("DB/user_credentials_db.txt", "r") as file:
        for line in file:
            user, pwd = line.strip().split(", ")
            if user == username and pwd == password:
                with open("DB/current_users.txt", "w") as f:
                    f.write(username)
                render_products_screen()
                return

    render_login_screen(error="Invalid username/Password")

def register(**user):
    if user["username"] == "" or user["password"] == "" or user["first_name"] == "" or user["last_name"] == "":
        render_register_screen(error="Please enter all required fields")
        return

    if user["username"] == user["password"]:
        render_register_screen(error="Username and Password cannot be same")
        return

    if len(user["password"]) < 6:
        render_register_screen(error="Password must be at least 6 characters")
        return

    if len(user["username"]) < 4:
        render_register_screen(error="Username must be at least 4 characters")
        return

    user.update({"products": []})
    with open("DB/user_credentials_db.txt", "r+") as file:
        users = [line.strip().split(", ")[0] for line in file]
        if user["username"] in users:
            render_register_screen(error="User already exists")
            return
        file.write(f"{user['username']}, {user['password']}\n")
    with open("DB/users.txt", "a") as file:
        file.write(json.dumps(user) + "\n")

    render_login_screen()

def render_login_screen(error=None):
    clean_screen()
    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)

    tk.Button(
        app,
        text="Enter",
        foreground="black",
        background="green",
        command=lambda: login(username.get(), password.get())
    ).grid(row=2, column=0)

    if error:
        tk.Label(app, text=error, fg="red").grid(row=3, column=0)

def render_register_screen(error=None):
    clean_screen()

    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)
    first_name = tk.Entry(app)
    first_name.grid(row=2, column=0)
    last_name = tk.Entry(app)
    last_name.grid(row=3, column=0)

    tk.Button(app,
              text="Register",
              foreground="black",
              background="green",
              command=lambda: register(
                  username=username.get(),
                  password=password.get(),
                  first_name=first_name.get(),
                  last_name=last_name.get()
              )).grid(row=4, column=0)

    if error:
        tk.Label(app, text=error, fg="red").grid(row=5, column=0)

def render_main_enter_screen():
    clean_screen()

    tk.Button(
        app,
        text="Login",
        foreground="white",
        background="green",
        command=render_login_screen
              ).grid(row=0, column=0)

    tk.Button(
        app,
        text="Register",
        foreground="black",
        background="yellow",
        command=render_register_screen
            ).grid(row=0, column=1)