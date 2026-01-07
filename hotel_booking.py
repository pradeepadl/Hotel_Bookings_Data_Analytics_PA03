import pandas as pd
import numpy as np

df= pd.read_csv('hotel_bookings.txt',delimiter='\t')
df.head()

    # Remove rows with missing values in 'Room number' column and set 'Text Value' to 'Date' where 'Room number' is NaN
df["Text Value"] = np.where(df["Room number"].isna(), df["Date"], np.nan)
df.head()
df["Text Value"].fillna(method='bfill', inplace=True)
df.dropna(inplace=True)
df.tail()