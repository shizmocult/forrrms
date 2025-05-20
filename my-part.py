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