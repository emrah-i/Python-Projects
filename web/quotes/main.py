import pytesseract
from PIL import Image
import sqlite3
import os

db = sqlite3.connect('web/quotes/quotes.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS quotes
                  (id INTEGER PRIMARY KEY, quote STRING, author STRING)''')


folder_path = 'web/quotes/favorite_quotes'

for file in os.listdir(folder_path):
    img_path = os.path.join(folder_path, file)
    with Image.open(img_path) as image:
        text = pytesseract.image_to_string(image)
        parts = text.replace('|', 'I').replace('\n', ' ').replace('"  ', '"').replace(' -- ', ' ').replace('"', '').split('--')
        cursor.execute("INSERT INTO quotes (quote, author) VALUES (?, ?)", (parts[0], parts[1]))
        db.commit()
