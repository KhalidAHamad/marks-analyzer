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

def get_grade_ranges():
    """
    FILL IT
    """
    ranges = [str(i) + '-' + str(i + 9) for i in range(10, 91, 10)]
    ranges.insert(0, "0-9")
    ranges.append("100")

    return ranges


def get_grades_frequency(grades):
    """

    """

    freq = [0] * 11

    for grade in grades:
        grade = int(grade // 10)
        freq[grade] += 1

    return freq


