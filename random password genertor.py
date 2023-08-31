import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_click():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError
        password = generate_random_password(length)
        messagebox.showinfo("Generated Password", f"Your generated password:\n{password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid password length.")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create GUI components
length_label = tk.Label(root, text="Enter password length:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_password_button_click)

# Place components in the window
length_label.pack()
length_entry.pack()
generate_button.pack()

# Start the GUI event loop
root.mainloop()
