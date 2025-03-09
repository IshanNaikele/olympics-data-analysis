import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

data=pd.read_csv(r'C:\Users\ISHAN\OneDrive\Desktop\Olympics Data analysis\Data\athlete_events.csv' )
region_data=pd.read_csv(r'C:\Users\ISHAN\OneDrive\Desktop\Olympics Data analysis\Data\noc_regions.csv')

df=preprocessor.preprocess(data,region_data)
st.sidebar.title("Olympics Analysis")

user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis ','Country Wise Analysis','Athelete Wise Analysis')
)


# st.dataframe(df)

# medal_tally=helper.medals_tally(df)
# print(medal_tally.columns)
 

if user_menu=='Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country=helper.country_year_list(df)
    selected_years=st.sidebar.selectbox("Select Year ",years)
    selected_country=st.sidebar.selectbox("Select Country ",country)
    medal_tally = helper.fetch_medal_tally(df,selected_years,selected_country)
    if selected_country == 'Overall' and selected_years == 'Overall':
        st.title("Overall Tally")
    elif selected_country == 'Overall' and selected_years != 'Overall':
        st.title(f"Medal Tally in {selected_years} Olympics ")
    elif selected_country != 'Overall' and selected_years == 'Overall':
        st.title(f"Medal Tally in {selected_country} Olympics ")
    elif selected_country != 'Overall' and selected_years != 'Overall':
        st.title(f"Medal Tally in year {selected_years} and country {selected_country} Olympics ")
    
    st.table(medal_tally)


if user_menu == 'Overall Analysis ':
    st.sidebar.header("Overall Analysis")
    editions=len(df['Year'].unique())-1
    cities=len(df['City'].unique())
    sports=len(df['Sport'].unique())
    events=len(df['Event'].unique())
    name=len(df['Name'].unique())
    nations=len(df['region'].unique())
     
    st.title("Top Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.header('Events')
        st.title(events)
    with col5:
        st.header('Nations')
        st.title(nations)
    with col6:
        st.header('Atheletes')
        st.title(name)


    nation_data=helper.nation_participated(df)
    fig=px.line(nation_data,x='Year',y='count')
    fig.update_layout(xaxis_title="Olympic Year",yaxis_title="Number of Participants")
    st.title("Participating nations over the time")
    st.plotly_chart(fig)

    events_data=helper.event_happened(df)
    fig=px.line(events_data,x='Year',y='count')
    fig.update_layout(xaxis_title="Olympic Year",yaxis_title="Number of Events")
    st.title("Events  over the time")
    st.plotly_chart(fig)

    atheletes_data=helper.atheletes_over_time(df)
    fig=px.line(atheletes_data,x='Year',y='count')
    fig.update_layout(xaxis_title="Olympic Year",yaxis_title="Number of Events")
    st.title("Atheletes Participated  over the time")
    st.plotly_chart(fig)

    events_heatmap=helper.events_heatmap(df)
    fig,ax=plt.subplots(figsize=(35,35))
    ax=sns.heatmap(events_heatmap.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype('int'),annot=True)
    st.title("Number of Events in Sports ")
    st.pyplot(fig)
 
    
    st.title("Most Successful Athletes")
    sports_data=df['Sport'].unique().tolist()
    sports_data.sort()
    sports_data.insert(0,'Overall')
    selected_sports=st.selectbox('Select a Sport',sports_data)
    x=helper.most_successful(df,selected_sports)
    st.table(x)


if user_menu == 'Country Wise Analysis':
    st.sidebar.title("Country Wise Analysis")
    region_data=df['region'].dropna().unique().tolist()
    region_data.sort()
     
    selected_region=st.sidebar.selectbox('Select a Sport',region_data)
    final_df=helper.yearwise_medal_tally(df,selected_region)
    st.title(f"{selected_region} Medals per Year")
    fig=px.line(final_df,x='Year',y='Medal')
    st.plotly_chart(fig)

    # Assuming df is your DataFrame and helper is a module with the country_medal_heatmap function
    pt = helper.country_medal_heatmap(df, selected_region)

    # Create a figure with a more reasonable size
    fig, ax = plt.subplots(figsize=(20, 10))  # Adjust the size as needed

    # Create the heatmap with better readability
    ax = sns.heatmap(
        pt,
        annot=True,  # Show values in the cells
        annot_kws={"size": 12},  # Adjust the font size of annotations
        fmt=".1f",  # Format annotations to one decimal place
        cmap="viridis",  # Use a better color map
        linewidths=0.5,  # Add lines between cells for better separation
        cbar_kws={"shrink": 0.8},  # Adjust the size of the color bar
    )

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha="right", fontsize=12)
    plt.yticks(fontsize=12)

    # Add labels and title
    ax.set_xlabel("X-Axis Label", fontsize=14)
    ax.set_ylabel("Y-Axis Label", fontsize=14)
    ax.set_title(f"Overall {selected_region} Country Performance in Olympics", fontsize=16, pad=20)

    # Display the plot in Streamlit
    st.title(f"Overall {selected_region} Country Performance in Olympics")
    st.pyplot(fig)

    st.title(f"Most Successful Athletes in {selected_region}")
    x=helper.most_successful_countrywise(df,selected_region)
    st.table(x)
        
if user_menu == 'Athelete Wise Analysis':
    st.sidebar.title("Athlete Wise Analysis")
    athletes_data = helper.athletes_data(df)
    
    # Extract age data for different medal categories
    x1 = athletes_data['Age'].dropna()
    x2 = athletes_data[athletes_data['Medal'] == 'Gold']['Age'].dropna()
    x3 = athletes_data[athletes_data['Medal'] == 'Silver']['Age'].dropna()
    x4 = athletes_data[athletes_data['Medal'] == 'Bronze']['Age'].dropna()
    
    # Create the distribution plot
    fig = ff.create_distplot(
        [x1, x2, x3, x4],
        ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
        show_hist=False,
        show_rug=False,
        colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Custom colors
    )
    
    # Update layout for better readability
    fig.update_layout(
        title='Age Distribution of Athletes by Medal Category',
        xaxis_title='Age',
        yaxis_title='Density',
        legend_title='Medal Category',
        font=dict(size=12),
        width=800,  # Adjust width
        height=500,  # Adjust height
        template='plotly_white'  # Use a clean template
    )
    
    # Increase line width for better visibility
    for trace in fig['data']:
        trace['line']['width'] = 2
    
    # Display the chart
    st.plotly_chart(fig)


    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athletes_data[athletes_data['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

     

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)


