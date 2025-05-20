import tkinter as tk
from tkinter import  messagebox, scrolledtext

def load_form_description(self):
    try:
        with open(self.form_file, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    name, field_type = line.rsplit(' ', 1)
                    self.fields.append((name, field_type))
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося завантажити форму: {e}")


def save_to_file(self, filename='data.txt'):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            formatted_data = [f'"{name}","{value}"' for name, value in self.form_data]
            file.write(','.join(formatted_data) + '\n')
        return True
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося зберегти дані: {e}")
        return False


def show_saved_data(self):
    try:
        with open('data.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()

        top = tk.Toplevel(self.master)
        top.title("Збережені дані")

        text = scrolledtext.ScrolledText(top, width=60, height=20)
        text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for line in data:
            text.insert(tk.END, line)

        text.config(state=tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося завантажити дані: {e}")
