import pandas as pd 
import numpy as np 
 

def get_medal_tally(data ):

    # data=data[data['Season']=='Summer']
    # data=data.merge(region_data,on='NOC',how='left')
    # data.drop_duplicates(inplace=True)
    # data=pd.concat([data,pd.get_dummies(data['Medal'])],axis=1)


    medal_tally=data.drop_duplicates(subset=['NOC','Games','Year','City','Sport','Event','Medal'])
    medal_tally=medal_tally.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    medal_tally['Total Medals']=medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']
    medal_tally['Gold']=medal_tally['Gold'].astype('int')
    medal_tally['Silver']=medal_tally['Silver'].astype('int')
    medal_tally['Bronze']=medal_tally['Bronze'].astype('int')
    medal_tally['Total Medals']=medal_tally['Total Medals'].astype('int')
    return medal_tally

 

def country_year_list(data):
    years=data['Year'].unique().tolist()
    years.sort()
    years.insert(0,"Overall")
    temp=data['region'].dropna()
    country=temp.unique().tolist()
    country.sort()
    country.insert(0,"Overall")

    return years,country

def fetch_medal_tally(df,year='Overall',country='Overall'):
    flag=0
    medal_data=df.drop_duplicates(subset=['NOC','Games','Year','City','Sport','Event','Medal'])
    if year == 'Overall' and country == 'Overall':
        temp_df=medal_data
    if year == 'Overall' and country != 'Overall':
        flag=1
        temp_df=medal_data[medal_data['region']==country]
    if year != 'Overall' and country == 'Overall':
        temp_df=medal_data[medal_data['Year']==int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df=medal_data[(medal_data['Year']==int(year) ) & (medal_data['region']==country)]

    if flag ==1 :
        temp_df=temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year',ascending=True).reset_index()
    else :
        temp_df=temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    
    temp_df['Total Medals']=temp_df['Gold']+temp_df['Silver']+temp_df['Bronze']
    temp_df['Gold']=temp_df['Gold'].astype('int')
    temp_df['Silver']=temp_df['Silver'].astype('int')
    temp_df['Bronze']=temp_df['Bronze'].astype('int')
    temp_df['Total Medals']=temp_df['Total Medals'].astype('int')
    return temp_df
    
def nation_participated(data):
    nation_data=data.drop_duplicates(['region','Year'])['Year'].value_counts().reset_index().sort_values('Year')
    return nation_data

   
def event_happened(data):
    events_data=data.drop_duplicates(['Event','Year'])['Year'].value_counts().reset_index().sort_values('Year')
    return  events_data

def atheletes_over_time(data):
    atheletes_data=data.drop_duplicates(['Name','Year'])['Year'].value_counts().reset_index().sort_values('Year')
    return  atheletes_data

 
def events_heatmap(data):
    x=data.drop_duplicates(['Year','Sport','Event'])
    return x
 


def most_successful(df,sport):
    temp_df=df.dropna(subset=['Medal'])
    if sport != 'Overall':
        temp_df=temp_df[temp_df['Sport']==sport]

    x=temp_df['Name'].value_counts().reset_index().head(15).merge(df,left_on='Name',right_on='Name',how='left')[['region','Name','count','Sport']]
    x=x.drop_duplicates('Name')
    x.rename(columns={'count':'No of Medals'},inplace=True)
    return x


def yearwise_medal_tally(data,country):
    data_new=data.dropna(subset=['Medal'])
    data_new.drop_duplicates(subset=['Sport','Event','City','Medal','Year','Games','region','Team'],inplace=True)
    data_new=data_new[data_new['region']== country]
    final_df=data_new.groupby('Year').count()['Medal'].reset_index()

    return final_df

def country_medal_heatmap(data,country):
    data_new=data.dropna(subset=['Medal'])
    data_new.drop_duplicates(subset=['Sport','Event','City','Medal','Year','Games','region','Team'],inplace=True)
    data_new=data_new[data_new['region']== country]
    data_new=data_new.pivot_table(index='Sport',columns='Year',values='Medal',aggfunc='count').fillna(0).astype('int') 
    return data_new


def most_successful_countrywise(df,country):
    temp_df=df.dropna(subset=['Medal'])
    if  country!= 'Overall':
        temp_df=temp_df[temp_df['region']==country]

    x=temp_df['Name'].value_counts().reset_index().head(15).merge(df,left_on='Name',right_on='Name',how='left')[['region','Name','count','Sport']]
    x=x.drop_duplicates('Name')
    x.rename(columns={'count':'No of Medals'},inplace=True)
    return x


def athletes_data(data):
    athletes_data=data.drop_duplicates(subset=['Name','region'] )
    return athletes_data


def weight_v_height(df,sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    athlete_df['Medal'].fillna('No Medal', inplace=True)
    if sport != 'Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        return temp_df
    else:
        return athlete_df

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)

    final.fillna(0, inplace=True)

    return final