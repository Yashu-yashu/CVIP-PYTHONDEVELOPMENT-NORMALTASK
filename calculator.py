import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Multiply':
            result = num1 * num2
        elif operation == 'Divide':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        else:
            return
        
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry fields
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

# Create operation dropdown
operation_var = tk.StringVar()
operation_var.set('Add')
operation_menu = tk.OptionMenu(root, operation_var, 'Add', 'Subtract', 'Multiply', 'Divide')

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)

# Create label to display result
result_label = tk.Label(root, text="Result:")

# Layout using grid
entry_num1.grid(row=0, column=0, padx=10, pady=10)
operation_menu.grid(row=0, column=1, padx=10, pady=10)
entry_num2.grid(row=0, column=2, padx=10, pady=10)
calculate_button.grid(row=1, columnspan=3, padx=10, pady=10)
result_label.grid(row=2, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
