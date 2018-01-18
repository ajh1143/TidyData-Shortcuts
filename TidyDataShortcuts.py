import pandas as pd
import matplotlib.pyplot as plt

#Melts a pandas DataFrame
def tidy_melt(df, exclude, var, value):
    df_melt = pd.melt(df, id_vars= exclude, var_name=var, value_name=value)
    return df_melt

#Returns a pivot table from a tidy df
def tidy_to_pivot(df, indices, colname, valname):
    df_piv = pd.pivot_table(df, index=indices, columns=colname, values=valname)
    return df_piv

#Returns a standard DataFrame from a tidydata set
def tidy_to_og(tidy_df):
    restored_df = tidy_df.reset_index()
    return restored_df
