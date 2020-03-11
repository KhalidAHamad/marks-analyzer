import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import sys



def get_mark_ranges():
    """
    Generates a list of ranges to be used in plotting

    >> get_mark_ranges()
    ["0-9", ...., "90-99", "100"]
    """
    ranges = [str(i) + '-' + str(i + 9) for i in range(10, 91, 10)]
    ranges.insert(0, "0-9")
    ranges.append("100")

    return ranges


def get_frequency(data_set):
    """ (pandas dataframe) -> list of int

    Returns a list of integers that represents the frequency of marks in
    a certain interval.
    """

    marks = data_set["mark"] # Will not get modified so no need to copy
    freq = []

    for i in range(11):
        mark_count = ((marks // 10) == i).sum()
        freq.append(mark_count)

    return freq


def get_mark_max(data_set):
    """(pandas dataframe) -> tuple([list of matric numbers], mark)

    Returns the matric numbers of the students who scored the highest mark and
    the mark.
    """

    try:
        max_mark = data_set["mark"].max(axis=0)
        students_max_mark = data_set[data_set["mark"] == max_mark]
        students_max_mark = students_max_mark["matric number"].to_list()
    except:
        print("One of the column names is invalid!")
        print("Make sure you have 2 columns with the following names:")
        print("\tmatric number\n\tmark")
        print("Aborting!")
        sys.exit()

    return students_max_mark, max_mark


def generate_report(avg_mark, median_mark, min_mark, max_mark,
                    students_max_mark):
    """
    Returns a formatted string containing the analysis report.
    """

    report = f"""The students scored an average mark of {avg_mark:.2f}.
The students' marks have a median of {median_mark:.2f}.
The lowest mark is {min_mark:.2f}.
The highest mark is {max_mark:.2f}, scored by:
{', '.join(students_max_mark)}."""

    return report


def plot_hist(bins, mark_count, mean_mark):
    """
    Plots a histogram of the students' marks distribution.
    """
    plt.style.use("seaborn")
    fig, ax = plt.subplots()
    ax.barh(bins, mark_count)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title("Students' Marks Histogram", color='darkblue', fontsize=17)
    ax.set_ylabel("Marks Distribution")
    ax.set_xlabel("Number of Students")
    print("** YOU HAVE TO CLOSE THE CHART IN ORDER FOR THIS PROGRAM TO "
          "CONTINUE EXECUTION! **")
    plt.show()

