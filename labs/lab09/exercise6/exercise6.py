import pandas as pd


def critical_inventory(filename):
    df = pd.read_csv(filename)
    critical_products = set(df.loc[(df.StockLevel<df.ReorderThreshold) & (df.DaysSinceRestock>30), 'ProductName'])
    result = {
        'total_products': len(df),
        'critical_count': len(critical_products),
        'critical_products' : critical_products
    }
    return result

critical_inventory('labs/lab09/data/inventory.csv')