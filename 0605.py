import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


class FormConstructor:
    def __init__(self, master, form_file):
        self.master = master
        self.form_file = form_file
        self.fields = []
        self.entries = []
        self.listboxes = []
        self.form_data = []

        self.load_form_description()
        self.create_form_widgets()

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

    def create_form_widgets(self):
        for i, (name, field_type) in enumerate(self.fields):

            label = tk.Label(self.master, text=name, anchor='w')
            label.grid(row=i, column=0, sticky='ew', padx=5, pady=5)

            if field_type == '{}':
                entry = tk.Entry(self.master)
                entry.grid(row=i, column=1, sticky='ew', padx=5, pady=5)
                self.entries.append((name, entry))
            elif field_type.startswith('[') and field_type.endswith(']'):
                options = field_type[1:-1].split(',')
                listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, exportselection=0, height=len(options))
                for option in options:
                    listbox.insert(tk.END, option)
                listbox.grid(row=i, column=1, sticky='ew', padx=5, pady=5)
                self.listboxes.append((name, listbox))
        self.create_control_buttons()

    def create_control_buttons(self):
        button_frame = tk.Frame(self.master)
        button_frame.grid(row=len(self.fields), column=0, columnspan=2, pady=10)

        self.next_btn = tk.Button(button_frame, text="Далі", command=self.save_and_continue)
        self.next_btn.pack(side=tk.LEFT, padx=5)

        self.done_btn = tk.Button(button_frame, text="Готово", command=self.save_and_show)
        self.done_btn.pack(side=tk.LEFT, padx=5)

        self.cancel_btn = tk.Button(button_frame, text="Відмінити", command=self.cancel)
        self.cancel_btn.pack(side=tk.LEFT, padx=5)

    def get_form_data(self):
        data = []
        for name, entry in self.entries:
            data.append((name, entry.get()))

        for name, listbox in self.listboxes:
            selection = listbox.curselection()
            if selection:
                data.append((name, listbox.get(selection[0])))
            else:
                data.append((name, ""))

        return data

    def save_to_file(self, filename='data.txt'):
        try:
            with open(filename, 'a', encoding='utf-8') as file:
                formatted_data = [f'"{name}","{value}"' for name, value in self.form_data]
                file.write(','.join(formatted_data) + '\n')
            return True
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося зберегти дані: {e}")
            return False

    def clear_form(self):
        for _, entry in self.entries:
            entry.delete(0, tk.END)

        for _, listbox in self.listboxes:
            listbox.selection_clear(0, tk.END)

    def save_and_continue(self):
        self.form_data = self.get_form_data()
        if self.save_to_file():
            self.clear_form()

    def save_and_show(self):
        self.form_data = self.get_form_data()
        if self.save_to_file():
            self.show_saved_data()

    def cancel(self):
        self.clear_form()

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


class FormsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Форма введення даних")

        self.menu_bar = tk.Menu(root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Відкрити файл", command=self.open_file)
        self.file_menu.add_command(label="Закрити", command=root.quit)
        self.menu_bar.add_cascade(label="Меню", menu=self.file_menu)

        root.config(menu=self.menu_bar)

        self.form_frame = tk.Frame(root)
        self.form_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.load_form('form1.txt')

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Виберіть файл форми",
            filetypes=(("Текстові файли", "*.txt"), ("Усі файли", "*.*"))
        )
        if file_path:
            self.load_form(file_path)

    def load_form(self, form_file):

        for widget in self.form_frame.winfo_children():
            widget.destroy()

        try:
            self.form = FormConstructor(self.form_frame, form_file)
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося завантажити форму: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FormsGUI(root)
    root.mainloop()
