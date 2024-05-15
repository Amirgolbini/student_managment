import mysql.connector
import tkinter.messagebox as messagebox


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'amir1382',
        database = 'student_management'
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
         except mysql.connector.Error as err :
             messagebox.showerror("Error",f"Database error:{err}")
             return None

