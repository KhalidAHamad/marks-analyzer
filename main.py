"""
Preconditions:
    - The file is an excel or csv file.
    - there are at least 2 columns with following names:
        matric number
        grade
"""

import analyze
import pandas as pd
import tkinter as tk
import os


# Handles wheather the file is xlsx or csv file
grades_file = tk.filedialog.askopenfilename(
        title="Select file", filetypes=(
            ("excel spreadsheets","*.xlsx"),
            ("comma seperated files", "*.csv"),
            ("all files","*.*"),
        )
    )

# file_name = "test_files/grades_small.csv"
file_extension = grades_file.split('.')[-1]
print(file_extension)

if file_extension == "xlsx":
    grades = pd.read_excel(grades_file)
elif file_extension == "csv":
    grades = pd.read_csv(grades_file)
else:
    print("Unsupported file type. Aborting!")
    exit()


grades.columns = grades.columns.str.strip().str.lower().str.replace("  ", " ")


students_max_grade, max_grade = analyze.get_grade_max(grades)
avg_grade = grades["grade"].mean(axis=0)
median_grade = grades["grade"].median(axis=0)

analyze.write_report(avg_grade, median_grade, max_grade, students_max_grade)

grade_count = analyze.get_frequency(grades)
grade_ranges = analyze.get_grade_ranges()

analyze.plot_hist(grade_ranges, grade_count, avg_grade)

