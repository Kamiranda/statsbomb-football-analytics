import pandas as pd
import numpy as np

#function to extract the coordinates of the events and create new columns with the x and y coordinates
def coordinates(df):
    cols = [col for col in df.columns if col.__contains__('location')]
    cols_x = [col + '_x' for col in df.columns if col.__contains__('location')]
    cols_y = [col + '_y' for col in df.columns if col.__contains__('location')]
    
    for i in range(len(cols)):
        df[cols_x[i]] = df[cols[i]].replace(np.nan,0).apply(lambda x: x[0] if x != 0 else np.nan)
        df[cols_y[i]] = df[cols[i]].replace(np.nan,0).apply(lambda x: x[1] if x != 0 else np.nan)
    
    df.drop(columns=cols, axis=1, inplace=True)
    
    return df