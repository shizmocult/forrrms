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