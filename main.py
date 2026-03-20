# Stuarrt Boekelman
# 3/19/2025
# Stock Bot

# Imports
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas as pd
from datetime import datetime
from polygon import RESTClient
import os
from dotenv import load_dotenv
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def resourcePath(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")  # Normal script execution
    return os.path.join(base_path, relative_path)

# Load environment variables
load_dotenv("api.env")
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API Key is missing! Make sure 'api.env' is in the same folder.")

client = RESTClient(API_KEY)

# Function to fetch stock data from Polygon
def fetch_stock_data():
    ticker = stock_entry.get().strip().upper()
    date_input = date_entry.get().strip()

    if not ticker or not date_input:
        messagebox.showerror("Error", "Please enter both ticker and date.")
        return

    try:
        date = datetime.strptime(date_input, '%m-%d-%Y').strftime('%Y-%m-%d')
        aggs = client.get_aggs(ticker, 1, "day", date, date)

        data = [
            [ticker, date, bar.open, bar.high, bar.low, bar.close, bar.volume]
            for bar in aggs
        ]

        if not data:
            messagebox.showinfo("No Data", f"No data available for {ticker} on {date}")
            return

        df = pd.DataFrame(data, columns=["Ticker", "Date", "Open", "High", "Low", "Close", "Volume"])
        display_data(df)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")

# Function to display data in the table
def display_data(data):
    for row in tree.get_children():
        tree.delete(row)

    for _, row in data.iterrows():
        tree.insert("", "end", values=(row['Ticker'], row['Date'], row['Open'], row['High'], row['Low'], row['Close'], row['Volume']))

# GUI Setup
root = tk.Tk()
root.title("Stock Bot")
root.geometry("700x400")

# Use resourcePath to load the icon correctly
try:
    icon_path = resourcePath("man.ico")
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Failed to load icon: {e}")

# Load background image
try:
    bg_image = Image.open(resourcePath("stonks.jpg"))
    bg_image = bg_image.resize((700, 200), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(root, width=700, height=200)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    canvas.pack()
except Exception as e:
    print(f"Failed to load background image: {e}")

frame = ttk.Frame(root)
frame.place(x=150, y=50)  # Adjust position based on background image

# Ticker Input
ticker_label = ttk.Label(frame, text="Enter Ticker:")
ticker_label.grid(row=0, column=0, padx=5, pady=5)
stock_entry = ttk.Entry(frame)
stock_entry.grid(row=0, column=1, padx=5, pady=5)

# Date Input (Month-Day-Year)
date_label = ttk.Label(frame, text="Enter Date (MM-DD-YYYY):")
date_label.grid(row=1, column=0, padx=5, pady=5)
date_entry = ttk.Entry(frame)
date_entry.grid(row=1, column=1, padx=5, pady=5)

# Fetch Button
fetch_button = ttk.Button(frame, text="Fetch Data", command=fetch_stock_data)
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

# Treeview (Data Table)
columns = ("Ticker", "Date", "Open", "High", "Low", "Close", "Volume")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(expand=True, fill="both")

root.mainloop()

if __name__ == '__main__':
    root.mainloop()
