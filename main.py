import tkinter as tk

import mysql.connector
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
<<<<<<< HEAD
            # messagebox.showinfo("success", "Student added successfully!")
=======
>>>>>>> 5bed0d28272b8076ad726d2aa0abf3e56f15cd33
            self.database.add_student(person)
            self.clear_entries()
            # messagebox.showinfo("Success", "Student added successfully!")
        else:
            messagebox.showwarning('Error', "Please fill in all the fields ")

    def edit_student(self):
        if self.selected_student:
            edit_window = tk.Toplevel(self)
            edit_window.title("Edit Student")

            student_data = self.selected_student

            lbl_id = tk.Label(edit_window, text="Meli code:")
            lbl_id.grid(row=0, column=0, padx=10, pady=10)
            self.entry_edit_id = tk.Entry(edit_window, state='normal')
            self.entry_edit_id.grid(row=0, column=1, padx=10, pady=10)
            self.entry_edit_id.insert(tk.END, student_data[0])

            lbl_first_name = tk.Label(edit_window, text="First name:")
            lbl_first_name.grid(row=1, column=0, padx=10, pady=10)
            self.entry_edit_first_name = tk.Entry(edit_window)
            self.entry_edit_first_name.grid(row=1, column=1, padx=10, pady=10)
            self.entry_edit_first_name.insert(tk.END, student_data[1])

            lbl_last_name = tk.Label(edit_window, text="Last name:")
            lbl_last_name.grid(row=2, column=0, padx=10, pady=10)
            self.entry_edit_last_name = tk.Entry(edit_window)
            self.entry_edit_last_name.grid(row=2, column=1, padx=10, pady=10)
            self.entry_edit_last_name.insert(tk.END, student_data[2])

            lbl_last_age = tk.Label(edit_window, text="age :")
            lbl_last_age.grid(row=3, column=0, padx=10, pady=10)
            self.entry_edit_age = tk.Entry(edit_window)
            self.entry_edit_age.grid(row=3, column=1, padx=10, pady=10)
            self.entry_edit_age.insert(tk.END, student_data[3])

            lbl_email = tk.Label(edit_window, text="Email :")
            lbl_email.grid(row=4, column=0, padx=10, pady=10)
            self.entry_email = tk.Entry(edit_window)
            self.entry_email.grid(row=4, column=1, padx=10, pady=10)
            self.entry_email.insert(tk.END, student_data[4])

            btn_save = tk.Button(edit_window, text="Save Change",
                                 command=lambda: self.database.upadte_student(self.selected_student[0],
                                                                              Person(self.entry_edit_id.get(),
                                                                                     self.entry_edit_first_name.get(),
                                                                                     self.entry_edit_last_name.get(),
                                                                                     self.entry_edit_age.get(),
                                                                                     self.entry_email.get())))
            btn_save.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        else:
            messagebox.showwarning("Warning", "An error occurred ")

    def view_student(self):
        view_window = tk.Toplevel(self)
        view_window.title("View Student")

<<<<<<< HEAD
        title_lable = tk.Label(view_window, text="All Students", font=("ARIAL", 16))
        title_lable.pack(pady=10)
=======
        title_label = tk.Label(view_window, text="All Students", font=("ARIAL", 16))
        title_label.pack(pady=10)
>>>>>>> 5bed0d28272b8076ad726d2aa0abf3e56f15cd33

        student_grid = Treeview(view_window, columns=("meli", "first_name", "last_name", "age", "email"),
                                show="headings")

        student_grid.heading("meli", text="Meli Code")
<<<<<<< HEAD
        student_grid.heading("first_name", text="first_name")
        student_grid.heading("last_name", text="last_name")
        student_grid.heading("age", text="age")
        student_grid.heading("email", text="email")
=======
        student_grid.heading("first_name", text="First Name")
        student_grid.heading("last_name", text="Last Name")
        student_grid.heading("age", text="Age")
        student_grid.heading("email", text="Email")
>>>>>>> 5bed0d28272b8076ad726d2aa0abf3e56f15cd33
        student_grid['show'] = 'headings'

        def on_select(event):
            item_id = student_grid.selection()[0]
            self.selected_student = student_grid.item(item_id, 'values')

        student_grid.bind("<<TreeviewSelect>>", on_select)

        students = self.database.get_all_student()

        for student in students:
            student_grid.insert("", tk.END, values=student)

        student_grid.pack(fill=tk.BOTH, expand=True)

    def del_student(self):
        if self.selected_student:
            try:
                if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this this student?"):
                    meli_code = self.selected_student[0]
                    self.database.delete_student(meli_code)

                    self.selected_student = None


            except:
                messagebox.showerror("Error", "An error occurred while deleting student!")
        else:
            messagebox.showwarning("Warning", "Please select a student to delete!")

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

if __name__ == '__main__':
    app = StudentManagementApp()
    app.mainloop()
