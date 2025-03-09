import pandas as pd 
import numpy as np 

data=pd.read_csv(r'C:\Users\ISHAN\OneDrive\Desktop\Olympics Data analysis\Data\athlete_events.csv' )
region_data=pd.read_csv(r'C:\Users\ISHAN\OneDrive\Desktop\Olympics Data analysis\Data\noc_regions.csv')

def preprocess(data,region_data):
    data=data[data['Season']=='Summer']
    data=data.merge(region_data,on='NOC',how='left')
    data.drop_duplicates(inplace=True)
    data=pd.concat([data,pd.get_dummies(data['Medal'])],axis=1)

    return data
