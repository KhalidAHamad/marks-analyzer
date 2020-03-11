"""
Preconditions:
    - The file is an excel or csv file.
    - there are at least 2 columns with following names:
        matric number
        mark
"""

import analyze
import pandas as pd
import tkinter as tk
import time
import sys


def main():
    intro()
    input() # Pause till the user press Enter.

    # Get file name
    marks_file = tk.filedialog.askopenfilename(
            title="Select a csv/excel file", filetypes=(
                ("all files","*.*"),
                ("excel spreadsheets","*.xlsx"),
                ("comma seperated files", "*.csv"),
            )
        )

    file_extension = marks_file.split('.')[-1]

    if file_extension == "xlsx":
        marks = pd.read_excel(marks_file)
    elif file_extension == "csv":
        marks = pd.read_csv(marks_file)
    else:
        print("Unsupported file type. Aborting!")
        sys.exit()

    # cleaning up the column names
    marks.columns = (
                    marks.columns.str.strip()
                    .str.lower()
                    .str.replace("  ", " ")
                )


    # some statistics to be used in the report
    students_with_max_mark, max_mark = analyze.get_mark_max(marks)
    min_mark = marks["mark"].min(axis=0)
    avg_mark = marks["mark"].mean(axis=0)
    median_mark = marks["mark"].median(axis=0)


    analysis_result = analyze.generate_report(avg_mark, median_mark, min_mark,
                         max_mark, students_with_max_mark)
    print('#' * 30)
    print('\nAnalysis Report\n')
    print(analysis_result)
    print('#' * 30)
    time.sleep(1)

    print("\n\n** Display a histogram of the marks distribution? [yes/no]")
    if get_choice():
        mark_count = analyze.get_frequency(marks)
        mark_ranges = analyze.get_mark_ranges()
        analyze.plot_hist(mark_ranges, mark_count, avg_mark)

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
    """
    Displays a short intro and explanation of the app
    """
    print('\n' * 2, "*" * 29,
        "Welcome to the marks analyzer",
        "*" * 29, sep='\n')
    print(
        "\n\n   - This program only analyzes excel/csv files.\n"
        "   - This program assumes that there is 2 columns with the following"
        " names:\n"
        "\tmark\n"
        "\tmatric number\n"
        "\n\nPress ENTER to select your file"
    )


def get_choice():
    """
    Returns the user choice (yes or no) after validating the input
    """
    while True:
        choice = input("> ")
        choice = choice.strip().lower()

        if choice == 'y' or choice == 'yes':
            return True
        elif choice == 'n' or choice == 'no':
            return False


main()
