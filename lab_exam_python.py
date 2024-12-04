import pandas as pd
import numpy as np
# reading the csv file for operations:
df = pd.read_csv('AQI_Data.csv') 

# a) Displaying the first 8 rows :
print("First 8 rows of the AQI Data:")
print(df.head(8))

# b) Displaying the last 5 rows : 
print("Last 5 rows of the AQI Data:")
print(df.tail(5))

#  c) show dtype and number of non null values in each column :
print("showing the Data Type of and number of not null rows:")
print(df.info())

#  d) Compute mean of AQI : 
AQI_mean = np.mean(df['AQI'])

# Compute max of PM2.5 : 
PM25_max = np.max(df['PM2.5'])

# Compute min of PM10 : 
PM10_min = np.min(df['PM10'])

#printing the values :
print("Mean of AQI:", AQI_mean)
print("Max of PM2.5:", PM25_max)
print("Min of PM10:", PM10_min)

# create a pivot table to represent unique city : 
pivot_df = df.pivot_table(index='City', aggfunc='size', fill_value=0)

# save the pivot table to a csv file : 
pivot_df.to_csv('pivot.csv', index=True)

#printing the unique cities : 
print(pivot_df)

#making a data frame for maximum of PM2.5 for each city : 
pivot_df = df.pivot_table(index='City', values='PM2.5', aggfunc='max', fill_value=0)
pivot_df.to_csv('pivot.csv', index=True)


