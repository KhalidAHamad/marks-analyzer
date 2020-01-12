def get_grades(grades_file):
    """(opened_file) -> list of floats

    Return a list of the grades from the grades_file

    Preconditions: grades_file is a csv file
    """

    grades_file.readline() # Skip the header
    grades = []

    for row in grades_file:
        row = row.split(',')
        grade = row[-1]
        grades.append(float(grade.strip()))

    return grades

def generate_grade_ranges(grades):
    """
    FILL IT
    """
    ranges = [str(i) + '-' + str(i + 9) for i in range(10, 91, 10)]
    ranges.insert(0, "0-9")
    ranges.append("100")

    return ranges
