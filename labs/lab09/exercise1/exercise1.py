import pandas as pd


def explore_data(filename):
    df = pd.read_csv(filename)

    dict_statistics = {
        "total_students": len(df),
        "subjects": list(df.columns),
        "math_average": round(float(df["Math"].mean()), 1),
        "highest_math_student": df.loc[df["Math"].idxmax(), "Name"]
    }

    print (dict_statistics)

explore_data("labs/lab09/data/students.csv")