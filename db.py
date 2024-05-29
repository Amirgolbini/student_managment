import mysql.connector
import tkinter.messagebox as messagebox

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='amir1382',
            database='student_management')
        self.cursor = self.connection.cursor()

    def add_student(self, person):
        try:
            query = "INSERT INTO student(meli, first_name, last_name, age, email) VALUES (%s, %s, %s, %s, %s)"
            person_data = (person.meli, person.first_name, person.last_name, person.age, person.email)
            self.cursor.execute(query, person_data)
            self.connection.commit()
            messagebox.showinfo("Success", "Student added successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    def get_all_students(self):
        try:
            query = "SELECT * FROM student"
            self.cursor.execute(query)
            students = self.cursor.fetchall()
            return students
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
            return None

    def update_student(self, meli, person):
        try:
            query = """
                UPDATE student SET meli = %s, first_name = %s, last_name = %s, age = %s, email = %s
                WHERE meli = %s
            """
            new_data = (person.meli, person.first_name, person.last_name, person.age, person.email, meli)
            self.cursor.execute(query, new_data)
            self.connection.commit()
            messagebox.showinfo("Success", "Student updated successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")

    def delete_student(self, meli):
        try:
            query = "DELETE FROM student WHERE meli = %s"
            self.cursor.execute(query, (meli,))
            self.connection.commit()
            if self.cursor.rowcount > 0:
                messagebox.showinfo("Success", "Student deleted successfully")
            else:
                messagebox.showwarning("Warning", "Student not found")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
