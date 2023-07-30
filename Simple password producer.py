import tkinter as tk
import random
import string
import pyperclip

def generate_password(seed_account):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(10))
    return password

def show_password():
    seed_account = entry.get()
    password = generate_password(seed_account)
    password_label.config(text=f"Generated Password: {password}")
    pyperclip.copy(password)  # 将生成的密码复制到剪贴板

def go_back():
    password_label.config(text="")
    entry.delete(0, tk.END)

def create_password_window():
    password_window = tk.Tk()
    password_window.title("Password Generator")
    
    global entry
    entry = tk.Entry(password_window, font=("Arial", 16))
    entry.pack(pady=20)
    
    generate_button = tk.Button(password_window, text="Generate Password", font=("Arial", 14), command=show_password)
    generate_button.pack()
    
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
