import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(filename):
    df = pd.read_csv(filename)
    math_scores = df["Math"]

    plt.plot(df.index, math_scores)
    plt.xlabel("Student Index")
    plt.ylabel("Math Score")
    plt.title("Math Score Trends")
    plt.show()

    return len(df)

'''
Background:

Show how Math scores vary across all students using a line chart.

Task:

Write a function show_math_trend(filename) that:

Loads CSV
Extracts Math column
Creates line chart:
x-axis = student index (df.index)
y-axis = Math scores
xlabel = "Student Index"
ylabel = "Math Score"
title = "Math Score Trends"
Calls plt.show()
Returns number of students (for testing)

example
count = show_math_trend("data/students.csv")
# Chart window appears showing Math scores
print(count)  # 25
'''