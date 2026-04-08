import pandas as pd


def compare_averages(filename):
    df = pd.read_csv(filename)

    subject_averages = {
        "Math": round(float(df["Math"].mean()), 1),
        "Science": round(float(df["Science"].mean()), 1),
        "English": round(float(df["English"].mean()), 1)
    }

    dict_averages = dict(subject_averages)
    dict_averages["best_subject"] = max(subject_averages, key=subject_averages.get)
    dict_averages["worst_subject"] = min(subject_averages, key=subject_averages.get)


    print(dict_averages)

compare_averages("labs/lab09/data/students.csv")