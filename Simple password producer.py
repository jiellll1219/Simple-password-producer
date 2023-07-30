import tkinter as tk
import random
import string
import pyperclip

def generate_password(seed, password_length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    return password

def show_password():
    seed = seed_entry.get()
    password_length = length_entry.get()

    if not password_length.isdigit():
        password_length = random.randint(10, 20)
    else:
        password_length = int(password_length)

    password = generate_password(seed, password_length)
    password_label.config(text=f"Generated Password: {password}")
    pyperclip.copy(password)

def go_back():
    password_label.config(text="")
    seed_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)

def create_password_window():
    password_window = tk.Tk()
    password_window.title("Password Generator")
    
    seed_label = tk.Label(password_window, text="Seed (Optional):", font=("Arial", 14))
    seed_label.pack(pady=10)
    global seed_entry
    seed_entry = tk.Entry(password_window, font=("Arial", 16))
    seed_entry.pack(pady=5)
    
    length_label = tk.Label(password_window, text="Password Length (Optional):", font=("Arial", 14))
    length_label.pack(pady=10)
    global length_entry
    length_entry = tk.Entry(password_window, font=("Arial", 16))
    length_entry.pack(pady=5)
    length_entry.insert(0, "If not specified, a random length between 10 and 20 will be chosen.")
    
    generate_button = tk.Button(password_window, text="Generate Password", font=("Arial", 14), command=show_password)
    generate_button.pack(pady=20)
    
    global password_label
    password_label = tk.Label(password_window, text="", font=("Arial", 14))
    password_label.pack(pady=20)
    
    copy_button = tk.Button(password_window, text="Copy to Clipboard", font=("Arial", 14), command=lambda: pyperclip.copy(password_label.cget("text")[18:]))
    copy_button.pack(pady=10)
    
    back_button = tk.Button(password_window, text="Go Back", font=("Arial", 14), command=go_back)
    back_button.pack(pady=10)
    
    password_window.mainloop()

if __name__ == "__main__":
    create_password_window()
