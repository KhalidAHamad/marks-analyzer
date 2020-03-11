# Students' Marks Analayzer
---
## Introduction and motivation
Through the last 2 years in my university, I found some of my friends going
through large excel files just trying to compare their mark with the marks of
other students. Thus, I made this program to automate the process for my
classmates and my lecturers, as well.

---
## Preconditions
This is a very basic app written in Python3.8 that is capable of analyzing any
csv/excel file that obey the following conditions:
    - The file has 2 columns at least with the names: `matric number` and
      `mark`.
    - The file does NOT contain any lines before the column names (you can refer
      to the images below for further explanation).

---
## How it works
Once you select your file, a short report will be printed on the screen.
The short report will contain the following information:
- The average (mean) score.
- The median score.
- The minimum mark.
- The maximum mark.
- A list of students' matric numbers who scored the maximum mark.

After that, you will be given the option to see a histogram illustrating the
marks distribution. Finally, after you close the chart and tKinter window (if 
you do not know what I mean by the latter, do not worry, it is illustrated
below in pictures) you will be given the option to save the report above,
without the chart, to a text file.


The program expects a file structure similar to this

It will NOT work with the following structure, _no column names in the first line_

Pictures of the app after finishing

After selecting your file close the tKinter window (the window in the picture
below)


