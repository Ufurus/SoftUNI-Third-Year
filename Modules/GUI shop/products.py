from helpers import clean_screen
from canvas import app
from PIL import Image, ImageTk
from helpers import get_current_user

import tkinter as tk
import json
import os

base_folder = os.path.dirname(__file__)

def update_current_user(username, product_id):
    with open("DB/users.txt", "r+") as file:
        users = [json.loads(u.strip()) for u in file]
        for user in users:
            a = type(user)
            if user["username"] == username:
                user["products"].append(product_id)
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(u) + "\n" for u in users])
                return

def purchased_product(product_id):
    with open("db/products.txt", "r+") as file:
        products = [json.loads(p.strip()) for p in file]
        for product in products:
            if product["id"] == product_id:
                product["count"] -= 1
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(p) + "\n" for p in products])
                return

def buy_products(product_id):
    clean_screen()

    username = get_current_user()

    if username:
        update_current_user(username, product_id)
        purchased_product(product_id)

    render_products_screen()

def render_products_screen():
    clean_screen()

    with open("db/products.txt") as file:
        products = [json.loads(p.strip()) for p in file]
        products = [p for p in products if p["count"] > 0]
        products_per_line = 3
        rows_for_product = len(products[0])
        for index, product in enumerate(products):
            row = int(index // products_per_line) * rows_for_product
            column = index % products_per_line

            tk.Label(app, text=product["name"]).grid(row=row, column=column)

            img = Image.open(os.path.join(base_folder, "DB/images", product["img_path"])).resize((200, 200))
            photo_image = ImageTk.PhotoImage(img)
            img_label = tk.Label(app, image=photo_image)
            img_label.image = photo_image
            img_label.grid(row=row+1, column=column)

            tk.Label(app, text=product["count"]).grid(row=row+2, column=column)

            tk.Button(app,
                      text=f"Buy: {product['id']}",
                      command=lambda p=product['id']: buy_products(p)
                      ).grid(row=row+3, column=column)