import mysql.connector
import tkinter.messagebox as messagebox


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='0173276',
            database='student_management'
        )

        self.cursor = self.connection.cursor()

    def add_student(self, person):
        try:
            query = "INSERT INTO student(meli, First_name, Last_name,age,email)VALUES (%s,%s,%s,%s,%s)"
            person = (person.meli, person.first_name, person.last_name, person.age, person.email)
            self.cursor.execute(query, person)
            self.connection.commit()
            messagebox.showinfo("success", "Student added successfully")

        except Exception as e:
            print(e)
            messagebox.showwarning('Error', 'It can not to add to db.!')

    def get_all_student(self):
        try:
            query = "SELECT * FROM student"
            self.cursor.execute(query)
            students = self.cursor.fetchall()
            return students
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error:{err}")
            return None

    def upadte_student(self, student_id, person):
        try:
            query = """
                UPDATE student SET meli =%s, first_name = %s , last_name = %s,age =%s,email = %s
                WHERE meli = %s
                
            """
            person = (person.meli, person.first_name, person.last_name, person.age, person.email, student_id)
            self.cursor.execute(query, person)
            self.connection.commit()
            messagebox.showinfo("Success", "Student updated successfuolly!")
        except mysql.connector.Error as err:
            messagebox.showwarning("Error", f"Database error : {err}")

    def del_student(self, meli):
        try:
            query = "DELETE FROM students WHERE meli = %s"
            self.cursor.execute(query, (meli,))
            self.connection.comit()
            if self.cursor.rowcount > 0:
                messagebox.showinfo("Success", "Student deleted successfully!")
            else:
                messagebox.showwarning("Error", "Student not found")
        except mysql.connector.Error as err:
            messagebox.showwarning("Error", f"Database error:{err}")
