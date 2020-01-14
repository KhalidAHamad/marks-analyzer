import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator



def get_grade_ranges():
    """
    FILL IT
    """
    ranges = [str(i) + '-' + str(i + 9) for i in range(10, 91, 10)]
    ranges.insert(0, "0-9")
    ranges.append("100")

    return ranges


def get_frequency(data_set):
    """ (pandas dataframe) -> list of int

    Returns a list of integers that represents the frequency of grades in
    a certain interval

    """

    grades = data_set["grade"] # Will not get modified so no need to copy
    freq = []

    for i in range(11):
        grade_count = ((grades // 10) == i).sum()
        freq.append(grade_count)

    return freq


def get_grade_max(data_set):
    """(pandas dataframe) -> tuple([list of matric numbers], grade)

    """

    max_grade = data_set["grade"].max(axis=0)
    print(max_grade)
    studnts_max_grade = data_set[data_set["grade"] == max_grade]
    studnts_max_grade = studnts_max_grade["matric number"].to_list()

    return studnts_max_grade, max_grade


def write_report(avg_grade, median_grade, max_grade, students_max_grade):

    print(
f"""avg mark is {avg_grade},
Grades has a median of {median_grade},
heighest mark is {max_grade}, scored by:
{', '.join(students_max_grade)}."""
)


def plot_hist(bins, grade_count, mean_grade):

    plt.style.use("seaborn")
    fig, ax = plt.subplots()
    # plt.barh(bins, grade_count)
    ax.barh(bins, grade_count)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.show()
