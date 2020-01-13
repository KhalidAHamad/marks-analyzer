import analyze
import numpy as np

grades_file = open("test_files/grades_small.csv", "r")

# read a file and turn the grades into a list
grades = analyze.get_grades(grades_file)
print(grades)

# create a grades range
grade_ranges = analyze.get_grade_ranges()
print(grade_ranges)

# get a list contains grades frequencies 
grades_frequency = analyze.get_grades_frequency(grades)
print(grades_frequency)


# Generate the histogram
hist = {}
for key, value in zip(grade_ranges, grades_frequency):
    hist[key] = value


print("\n\n", hist)
