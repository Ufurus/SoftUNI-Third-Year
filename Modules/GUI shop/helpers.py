from canvas import tk
from canvas import app

def clean_screen():
    for el in app.grid_slaves():
        el.destroy()

def get_current_user():
    with open("DB/current_users.txt", "r") as file:
        return file.read().strip()