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
import time
import sys

# file_name = "test_files/grades_small.csv"
# print(file_extension)

def main():
    intro()
    input() # Pause till the user press Enter.

    # Get file name
    grades_file = tk.filedialog.askopenfilename(
            title="Select file", filetypes=(
                ("excel spreadsheets","*.xlsx"),
                ("comma seperated files", "*.csv"),
                ("all files","*.*"),
            )
        )

    file_extension = grades_file.split('.')[-1]

    if file_extension == "xlsx":
        grades = pd.read_excel(grades_file)
    elif file_extension == "csv":
        grades = pd.read_csv(grades_file)
    else:
        print("Unsupported file type. Aborting!")
        sys.exit()

    # cleaning up the column names
    grades.columns = (
                    grades.columns.str.strip()
                    .str.lower()
                    .str.replace("  ", " ")
                )


    students_with_max_grade, max_grade = analyze.get_grade_max(grades)
    avg_grade = grades["grade"].mean(axis=0)
    median_grade = grades["grade"].median(axis=0)


    analysis_result = analyze.generate_report(avg_grade, median_grade,
                         max_grade, students_with_max_grade)
    print('#' * 30)
    print(analysis_result)
    print('#' * 30)
    time.sleep(1)

    print("\n\n** Display a histogram of the grades distribution? [yes/no]")
    if get_choice():
        grade_count = analyze.get_frequency(grades)
        grade_ranges = analyze.get_grade_ranges()
        analyze.plot_hist(grade_ranges, grade_count, avg_grade)

    print("\n\n** Save the analysis result to a text (.txt) file? [yes/no]")
    if get_choice():
        report_file = tk.filedialog.asksaveasfilename(
                confirmoverwrite=False,
                defaultextension=".txt",
                filetypes=(("text file", "*.txt"), ("All Files", "*.*"))
            )
        report = open(report_file, 'a')
        report.write(analysis_result)
        report.close()
        print("\n\nDONE!")




def intro():
    print('\n' * 2, "*" * 29,
        "Welcome to the grade analyzer",
        "*" * 29, sep='\n')
    print(
        "\n\n   - This program only analyzes excel/csv files.\n"
        "   - This program assumes that there is 2 columns with the following"
        " names:\n"
        "\tgrade\n"
        "\tmatric number\n"
        "\n\nPress ENTER to select your file"
    )


def get_choice():
    while True:
        choice = input("> ")
        choice = choice.strip().lower()

        if choice == 'y' or choice == 'yes':
            return True
        elif choice == 'n' or choice == 'no':
            return False


main()
