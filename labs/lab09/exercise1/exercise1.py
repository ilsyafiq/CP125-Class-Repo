import pandas as pd


def explore_data(filename):
    df = pd.read_csv(filename)

    result = {
        "total_students": len(df),
        "subjects": list(df.columns[2:7]),
        "math_average": round(float(df["Math"].mean()), 1),
        "highest_math_student": df.loc[df["Math"].idxmax(), "Name"]
    }

    print (result)
    return result

explore_data("labs/lab09/data/students.csv")