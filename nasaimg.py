import requests
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

# Replace with your NASA API key
NASA_API_KEY = "OwPmaQUMi6Cjhj1eR9XkdnYYgPuK4gRnHiJLhLIf"

def fetch_apod_images(start_date, end_date):
    images = []

    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": NASA_API_KEY,
        "hd": "True",  # Request high-resolution images
    }

    current_date = start_date
    while current_date <= end_date:
        params["date"] = current_date.strftime("%Y-%m-%d")
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            images.append(data)

        current_date += timedelta(days=1)

    return images

def show_images():
    start_date = date_from_var.get()
    end_date = date_to_var.get()

    if not start_date or not end_date:
        return

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    images = fetch_apod_images(start_date, end_date)

    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)

    for image in images:
        result_text.insert(tk.END, f"Title: {image['title']}\n")
        result_text.insert(tk.END, f"Date: {image['date']}\n")
        result_text.insert(tk.END, f"Explanation: {image['explanation']}\n\n")

    result_text.config(state="disabled")

# Create the main window
window = tk.Tk()
window.title("NASA APOD Image Viewer")

# Create date picker fields
date_from_label = ttk.Label(window, text="Date from:")
date_from_label.pack()
date_from_var = tk.StringVar()
date_from_entry = ttk.Entry(window, textvariable=date_from_var)
date_from_entry.pack()

date_to_label = ttk.Label(window, text="Date to:")
date_to_label.pack()
date_to_var = tk.StringVar()
date_to_entry = ttk.Entry(window, textvariable=date_to_var)
date_to_entry.pack()

# Create a button to fetch APOD images
fetch_button = ttk.Button(window, text="Fetch APOD Images", command=show_images)
fetch_button.pack()

# Create a scrolled text widget to display the results
result_text = tk.Text(window, wrap=tk.WORD, width=60, height=15)
result_text.pack()
result_text.config(state="disabled")

window.mainloop()