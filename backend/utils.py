import pandas as pd

def is_nan(string):
    try:
        # Convert string to float and check if it is NaN
        return pd.isna(float(string))
    except ValueError:
        # If conversion fails, it's not NaN
        return False