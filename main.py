import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
from ttkbootstrap import Treeview
from db import Database
from students import Person

class StudentManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Student Management System")
        self.geometry("800x450")
        self.configure(bg="cadet blue")
        self.create_widgets()
        self.database = Database()

    def create_widgets(self):
        lbl_id = tk.Label(self, text='Meli code:', bg="firebrick1", fg="white")
        lbl_id.grid(row=0, column=0, padx=10, pady=10)

        lbl_first_name = tk.Label(self, text='First name:', bg="firebrick1", fg="white")
        lbl_first_name.grid(row=1, column=0, padx=10, pady=10)

        lbl_last_name = tk.Label(self, text='Last name:', bg="firebrick1", fg="white")
        lbl_last_name.grid(row=2, column=0, padx=10, pady=10)

        lbl_age = tk.Label(self, text='Age:', bg="firebrick1", fg="white")
        lbl_age.grid(row=3, column=0, padx=10, pady=10)

        lbl_email = tk.Label(self, text='Email:', bg="firebrick1", fg="white")
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

        btn_add = tk.Button(self, text='Add Student', command=self.add_student, bg="blue", fg="white")
        btn_add.grid(row=5, column=0, padx=10, pady=10)

        btn_edit = tk.Button(self, text='Edit Student', command=self.edit_student, bg="blue", fg="white")
        btn_edit.grid(row=5, column=1, padx=10, pady=10)

        btn_view = tk.Button(self, text='View Students', command=self.view_students, bg="blue", fg="white")
        btn_view.grid(row=6, column=0, padx=10, pady=10)

        btn_delete = tk.Button(self, text='Delete Student', command=self.delete_student, bg="blue", fg="white")
        btn_delete.grid(row=6, column=1, padx=10, pady=10)

        btn_clear = tk.Button(self, text='Clear Entries', command=self.clear_entries, bg="blue", fg="white")
        btn_clear.grid(row=7, column=0, padx=10, pady=10)

        image = Image.open("F:/J/IMG_۲۰۲۰۰۷۱۷_۲۰۱۵۰۲.jpg")
        image = image.resize((350, 200))
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(self, image=photo)
        image_label.image = photo
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
        else:
            messagebox.showwarning('Error', "Please fill in all the fields")

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

            lbl_age = tk.Label(edit_window, text="Age:")
            lbl_age.grid(row=3, column=0, padx=10, pady=10)
            self.entry_edit_age = tk.Entry(edit_window)
            self.entry_edit_age.grid(row=3, column=1, padx=10, pady=10)
            self.entry_edit_age.insert(tk.END, student_data[3])

            lbl_email = tk.Label(edit_window, text="Email:")
            lbl_email.grid(row=4, column=0, padx=10, pady=10)
            self.entry_edit_email = tk.Entry(edit_window)
            self.entry_edit_email.grid(row=4, column=1, padx=10, pady=10)
            self.entry_edit_email.insert(tk.END, student_data[4])

            btn_save = tk.Button(edit_window, text="Save Changes", command=self.save_student_changes)
            btn_save.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        else:
            messagebox.showwarning("Warning", "Please select a student to edit")

    def view_students(self):
        view_window = tk.Toplevel(self)
        view_window.title("View Students")

        title_label = tk.Label(view_window, text="All Students", font=("Arial", 16))
        title_label.pack(pady=10)

        student_grid = Treeview(view_window, columns=("Meli", "First Name", "Last Name", "Age", "Email"),
                                show="headings")

        student_grid.heading("Meli", text="Meli Code")
        student_grid.heading("First Name", text="First Name")
        student_grid.heading("Last Name", text="Last Name")
        student_grid.heading("Age", text="Age")
        student_grid.heading("Email", text="Email")

        student_grid['show'] = 'headings'

        def on_select(event):
            item_id = student_grid.selection()[0]
            self.selected_student = student_grid.item(item_id, 'values')

        student_grid.bind("<<TreeviewSelect>>", on_select)

        students = self.database.get_all_students()

        for student in students:
            student_grid.insert("", tk.END, values=student)

        student_grid.pack(fill=tk.BOTH, expand=True)

    def delete_student(self):
        if self.selected_student:
            # Create a confirmation message box
            confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this student?")

            # Check user's response
            if confirmation:
                meli_code = self.selected_student[0]
                self.database.delete_student(meli_code)
                self.view_students()
                self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please select a student to delete")

    def save_student_changes(self):
        meli = self.entry_edit_id.get()
        first_name = self.entry_edit_first_name.get()
        last_name = self.entry_edit_last_name.get()
        age = self.entry_edit_age.get()
        email = self.entry_edit_email.get()

        if meli and first_name and last_name and age and email:
            person = Person(meli, first_name, last_name, age, email)
            self.database.update_student(meli, person)
            messagebox.showinfo("Success", "Student information updated")
        else:
            messagebox.showwarning('Error', "Please fill in all the fields")

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

if __name__ == '__main__':
    app = StudentManagementApp()
    app.mainloop()
