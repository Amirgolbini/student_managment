import tkinter as tk


class StudentManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Student Management System")
        self.geometry("250x400")
        self.creat_widget()
        self.database = Database()

    def creat_widget(self):
        lbl_id = tk.Label(self, text='Meli code:')
        lbl_id.grid(row=0, column=0, padx=10, pady=10)

        lbl_last_name = tk.Label(self, text='Firts name:')
        lbl_last_name.grid(row=1, column=0, padx=10, pady=10)

        lbl_age = tk.Label(self, text='AGE:')
        lbl_age.grid(row=2, column=0, padx=10, pady=10)

        lbl_email = tk.Label(self, text='Email;')
        lbl_email.grid(row=4, column=0, padx=10, pady=10)



if __name__ == '__main__':
    app = StudentManagementApp()
    app.mainloop()
