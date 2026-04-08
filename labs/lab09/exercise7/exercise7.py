import pandas as pd


def promotion_candidates(filename):
    df = pd.read_csv(filename)
    average_performance = round(float(df["PerformanceScore"].mean()), 1)
    qualified = set(df.loc[(df.PerformanceScore>average_performance) & (df.YearsOfService>=2), "EmployeeName"])
    result = {
        "average_performance" : average_performance,
        "min_years_required" : 2,
        "candidate_count" : len(qualified),
        "candidate_names" : qualified
    }
    return result
promotion_candidates('labs/lab09/data/employees.csv')