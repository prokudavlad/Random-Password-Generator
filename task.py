import tkinter as tk
import string
import random

# Creating an window
root = tk.Tk()
root.title('Password generator')

# Creation of interface elements
length_label = tk.Label(root, text='Password length:')
length_entry = tk.Entry(root)
length_entry.insert(0, '8')  # default value
strength_label = tk.Label(root, text='Complexity:')
strength_var = tk.StringVar()
strength_combobox = tk.OptionMenu(root, strength_var, 'Easy', 'Medium', 'Difficult')
strength_var.set('Medium')  # default value
password_label = tk.Label(root, text='Generated password:')
password_entry = tk.Entry(root)

# Placement of interface elements in a window
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry.grid(row=0, column=1, padx=5, pady=5)
strength_label.grid(row=1, column=0, padx=5, pady=5)
strength_combobox.grid(row=1, column=1, padx=5, pady=5)
password_label.grid(row=2, column=0, padx=5, pady=5)
password_entry.grid(row=2, column=1, padx=5, pady=5)

# Function to generate a password
def generate_password():
    length = int(length_entry.get())
    strength = strength_var.get()

    # Defining characters for generating a password depending on its complexity
    if strength == 'Easy':
        characters = string.ascii_letters
    elif strength == 'Medium':
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + '@#$%^&*()_+=\'\|><~`'

    # Password generation
    password = ''.join(random.choice(characters) for i in range(length))

    # Displaying the password on the screen
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Creating a Generate Password Button
generate_button = tk.Button(root, text='Generate password', command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Running the main event loop
root.mainloop()
