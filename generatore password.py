import tkinter as tk
from tkinter import messagebox, ttk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Generatore di Password")

        self.length_label = tk.Label(master, text="Lunghezza:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.lowercase_var = tk.IntVar()
        self.lowercase_checkbutton = tk.Checkbutton(master, text="Minuscole", variable=self.lowercase_var)
        self.lowercase_checkbutton.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbutton = tk.Checkbutton(master, text="Maiuscole", variable=self.uppercase_var)
        self.uppercase_checkbutton.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.digits_var = tk.IntVar()
        self.digits_checkbutton = tk.Checkbutton(master, text="Numeri", variable=self.digits_var)
        self.digits_checkbutton.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.punctuation_var = tk.IntVar()
        self.punctuation_checkbutton = tk.Checkbutton(master, text="Caratteri Speciali", variable=self.punctuation_var)
        self.punctuation_checkbutton.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.generate_button = tk.Button(master, text="Genera Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.password_label = tk.Label(master, text="")
        self.password_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.copy_button = tk.Button(master, text="Copia Password", command=self.copy_password)
        self.copy_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        length = int(self.length_entry.get())
        lowercase = bool(self.lowercase_var.get())
        uppercase = bool(self.uppercase_var.get())
        digits = bool(self.digits_var.get())
        punctuation = bool(self.punctuation_var.get())

        if not (lowercase or uppercase or digits or punctuation):
            messagebox.showwarning("Attenzione", "Seleziona almeno un tipo di carattere.")
            return

        characters = ""
        if lowercase:
            characters += string.ascii_lowercase
        if uppercase:
            characters += string.ascii_uppercase
        if digits:
            characters += string.digits
        if punctuation:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=f"Password: {password}")

        # Memorizza la password generata per la copia
        self.generated_password = password

    def copy_password(self):
        if hasattr(self, 'generated_password'):
            self.master.clipboard_clear()
            self.master.clipboard_append(self.generated_password)
            messagebox.showinfo("Copia Password", "Password copiata negli appunti!")

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
