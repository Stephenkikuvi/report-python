import tkinter as tk
from tkinter import Text, Button
import mysql.connector

class ReportForm:
    def __init__(self, root, db_connection):
        self.root = root
        self.db_connection = db_connection
        self.root.title("Sign-Up Report")

        self.txt_report = Text(root, width=80, height=20)
        self.txt_report.grid(row=0, column=0, padx=10, pady=10)

        self.btn_generate = Button(root, text="Generate Report", command=self.generate_report)
        self.btn_generate.grid(row=1, column=0, padx=10, pady=5)

    def generate_report(self):
        # Clear previous report
        self.txt_report.delete(1.0, tk.END)

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM users")
        signups = cursor.fetchall()
        cursor.close()

        report_text = ""
        for signup in signups:
            report_text += f"Username: {signup[1]}, Email: {signup[3]}\n"

        self.txt_report.insert(tk.END, report_text)

def main():
    root = tk.Tk()
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pysignup"
    )
    report_form = ReportForm(root, db_connection)
    root.mainloop()
    db_connection.close()

if __name__ == "__main__":
    main()
