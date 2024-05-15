import tkinter as tk
from PIL import Image, ImageTk
from students import Person
import tkinter.messagebox as messagebox
from db import Database
from ttkbootstrap import Treeview

class StudentManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Student Management System")
        self.geometry("800x450")
        self.configure(bg="#ADD8E6")
        self.create_widgets()
        self.database = Database()

    # label field
    def create_widgets(self):
        lbl_id = tk.Label(self, text='Meli code:', bg="#9932CC", fg="white")
        lbl_id.grid(row=0, column=0, padx=10, pady=10)

        lbl_first_name = tk.Label(self, text='Firts name:', bg="#9932CC", fg="white")
        lbl_first_name.grid(row=1, column=0, padx=10, pady=10)

        lbl_last_name = tk.Label(self, text='last name:', bg="#9932CC", fg="white")
        lbl_last_name.grid(row=2, column=0, padx=10, pady=10)

        lbl_age = tk.Label(self, text='AGE:', bg="#9932CC", fg="white")
        lbl_age.grid(row=3, column=0, padx=10, pady=10)

        lbl_email = tk.Label(self, text='Email;', bg="#9932CC", fg="white")
        lbl_email.grid(row=4, column=0, padx=10, pady=10)

        self.entry_id = tk.Entry(self, width=50)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        self.entry_first_name = tk.Entry(self, width=50)
        self.entry_first_name.grid(row=1, column=1, padx=10, pady=10)

        self.entry_last_name = tk.Entry(self, width=50)
        self.entry_last_name.grid(row=2, column=1, padx=10, pady=10)

        self.entry_age = tk.Entry(self, width=50)
        self.entry_age.grid(row=3, column=1, padx=10, pady=10)

        self.entry_email = tk.Entry(self, width=50)
        self.entry_email.grid(row=4, column=1, padx=10, pady=10)

        btn_add = tk.Button(self, text='Add student:', command=self.add_student, bg="blue", fg="white")
        btn_add.grid(row=5, column=0, padx=10, pady=10)

        btn_edit = tk.Button(self, text='Edit student:', command=self.edit_student, bg="blue", fg="white")
        btn_edit.grid(row=5, column=1, padx=10, pady=10)

        btn_view = tk.Button(self, text='View student', command=self.view_student, bg="blue", fg="white")
        btn_view.grid(row=6, column=0, padx=10, pady=10)

        btn_delete = tk.Button(self, text='delet Student', command=self.del_student, bg="blue", fg="white")
        btn_delete.grid(row=6, column=1, padx=10, pady=10)

        btn_clear = tk.Button(self, text='Clear student', command=self.clear_entries, bg="blue", fg="white")
        btn_clear.grid(row=7, column=0, padx=10, pady=10)

        image = Image.open("F:/J/IMG_۲۰۲۰۰۷۱۷_۲۰۱۵۰۲.jpg")
        image = image.resize((350, 200))  # Resize the image
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        image_label = tk.Label(self, image=photo)
        image_label.image = photo  # Keep a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

    def add_student(self):
        meli = self.entry_id.get()
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        age = self.entry_age.get()
        email = self.entry_email.get()

        if meli and first_name and last_name and email:
            person = Person(meli, first_name, last_name, age, email)
            self.database.add_student(person)
            self.clear_entries()
            # messagebox.showinfo("Success", "Student added successfully!")
        else:
            messagebox.showwarning('Error', "Please fill in all the fields ")

    def edit_student(self):
        pass

    def view_student(self):
        view_window = tk.Toplevel(self)
        view_window.title("View Student")

        title_label = tk.Label(view_window, text="All Students", font=("ARIAL", 16))
        title_label.pack(pady=10)

        student_grid = Treeview(view_window, columns=("meli", "first_name", "last_name", "age", "email"),
                                show="headings")

        student_grid.heading("meli", text="Meli Code")
        student_grid.heading("first_name", text="First Name")
        student_grid.heading("last_name", text="Last Name")
        student_grid.heading("age", text="Age")
        student_grid.heading("email", text="Email")
        student_grid['show'] = 'headings'

        students = self.database.get_all_student()

        for student in students:
            student_grid.insert("", tk.END, values=student)

        student_grid.pack(fill=tk.BOTH, expand=True)

    def del_student(self):
        pass

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

if __name__ == '__main__':
    app = StudentManagementApp()
    app.mainloop()
