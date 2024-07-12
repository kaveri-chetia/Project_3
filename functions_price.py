import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#--------------------------------------------MERGE CSV FILES------------------------------------------------
def merge_csv_files(file_list):
    #create an empty list to store the dataframes
    dataframes = []
    # Loop through the list of files and read them into pandas
    for file in file_list:
        df = pd.read_csv(file)
        dataframes.append(df)
    
    #add quarter column for grouping
    for i in range(len(dataframes)):
        #remove the path and extract the file name
        filename = file_list[i].split('/')[-1]
        #split the filename by '_' and extract the quarter and year
        parts = filename.split('_')
        #extract the quarter and year and concatenate them
        quarter_year = f"{parts[2]}_{parts[3].split('.')[0]}"
        #add the quarter column to the dataframe
        dataframes[i]['quarter'] = quarter_year 

    #remove unnecessary columns
    for i in range(len(dataframes)):
        dataframes[i] = dataframes[i].drop(columns=[
                    'last_review',
                   'number_of_reviews_ltm',
                   'license',
                   'neighbourhood_group'
        ])

        #fill missing values in price column
        dataframes[i]['price'] = dataframes[i]['price'].fillna(dataframes[i]['price'].mean())
    
    #concatenate the dataframes
    merged_dataframe = pd.concat(dataframes, ignore_index=True)
    return merged_dataframe


#--------------------------------------------CREATE ONE DATAFRAME-----------------------------------------------

def merge_data_frames_currency(df_list):
    #create an empty list to store the merged dataframes for each city
    dataframes_merged = []
    # Loop through the list of data frames (df_list defined below) and append them to the empty list dataframes_merged
    for df in df_list:
        dataframes_merged.append(df)

    #add city column for grouping
    #define the city names
    city_names = ['Rome', 'Madrid', 'Barcelona', 'Istanbul', 'London', 'Paris']
    #loop through the dataframes
    for i in range(len(df_list)):
        #add city column by matching the index of the city_names list with the index of the dataframes in the df_list
        df_list[i]['city'] = city_names[i]

    #add currency column
    #define the currency values
    currency_values = ['EUR', 'EUR', 'EUR', 'TRY', 'GBP', 'EUR']
    #loop through the dataframes
    for i in range(len(df_list)):
        #add currency column by matching the index of the currency_values list with the index of the dataframes in the df_list
        df_list[i]['currency'] = currency_values[i]

    
    #concatenate the dataframes
    final_dataframe = pd.concat(dataframes_merged, ignore_index=True)

    #move currency column next to price column
    col = final_dataframe.pop('currency')
    final_dataframe.insert(9, 'currency', col)

    return final_dataframe


#--------------------------------------------GETTING EXCHANGE RATES------------------------------------------------

def get_exchange_rates():
    API_KEY = os.getenv('EXCHANGERATE_API_KEY')
    BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/EUR'
    response = requests.get(BASE_URL)
    data = response.json()
    if data['result'] == 'error':
        raise Exception(data['error-type'])
    return data['conversion_rates']


#--------------------------------------------VISUALISE PRICE DISTRIBUTION------------------------------------------------


def visualize_price_distribution_with_outliers(dataframe, cities):
    city_dataframes = {}
    for city in cities:
        city_data = dataframe[dataframe['city'] == city]
        city_dataframes[city] = city_data
        city_data = dataframe[dataframe['city'] == city]
        plt.figure(figsize=(5, 3))
        sns.boxplot(x='quarter', y='price_in_eur', data=city_data)
        plt.title(f'Price Distribution per Quarter: {city}')
        plt.xlabel('Quarter')
        plt.ylabel('Price in EUR')
        plt.show()
    

def visualize_price_distribution_without_outliers(dataframe, cities):
    city_dataframes = {}
    for city in cities:
        city_data = dataframe[dataframe['city'] == city]
        city_dataframes[city] = city_data
        city_data = dataframe[dataframe['city'] == city]
    
        # Calculate Q1 (25th percentile) and Q3 (75th percentile)
        Q1 = city_data['price_in_eur'].quantile(0.25)
        Q3 = city_data['price_in_eur'].quantile(0.75)
        IQR = Q3 - Q1

        # Define outlier bounds
        lower_bound = max(Q1 - 1.5 * IQR, 5)
        upper_bound = Q3 + 1.5 * IQR

        # Remove outliers
        dataframe_no_outliers = city_data[(city_data['price_in_eur'] >= lower_bound) & (city_data['price_in_eur'] <= upper_bound)]

        # Create a histogram with no outliers
        fig = px.histogram(
            dataframe_no_outliers,
            x='price_in_eur',
            nbins=10,
            title=f'Prices in {city} (No Outliers)',
            labels={'price_in_eur': 'Price in EUR'},
            template='plotly_white'
        )

    # Customize the appearance
        fig.update_traces(marker=dict(color='skyblue', line=dict(color='black', width=1.5)))

    # Customize layout
        fig.update_layout(
            xaxis_title='Price in EUR',
            yaxis_title='Frequency',
            title_font_size=16,
            xaxis_title_font_size=14,
            yaxis_title_font_size=14,
            xaxis=dict(tickfont=dict(size=12)),
            yaxis=dict(tickfont=dict(size=12)),
            showlegend=True,
            width=600,  # Adjusted width to smaller size
            height=400
        )

        # Show the plot
        fig.show()

#--------------------------------------------CALCULATE STATS------------------------------------------------

def calculate_stats(df):
    stats = []
    cities = df['city'].unique()
    
    for city in cities:
        city_df = df[df['city'] == city]
        
        # Calculate Q1, Q3, and IQR
        Q1 = city_df['price_in_eur'].quantile(0.25)
        Q3 = city_df['price_in_eur'].quantile(0.75)
        IQR = Q3 - Q1
        
        # Define outlier bounds
        lower_bound = max(Q1 - 1.5 * IQR, 5)
        upper_bound = Q3 + 1.5 * IQR
        
        # Remove outliers
        city_no_outliers = city_df[(city_df['price_in_eur'] >= lower_bound) & (city_df['price_in_eur'] <= upper_bound)]
        
        # Calculate min, max, and mean prices
        min_price = round(city_no_outliers['price_in_eur'].min(), 2)
        max_price = round(city_no_outliers['price_in_eur'].max(), 2)
        mean_price = round(city_no_outliers['price_in_eur'].mean(), 2)
    
        
        stats.append({'city': city, 'min_price': min_price, 'max_price': max_price, 'mean_price': mean_price})
    
    return pd.DataFrame(stats)



#--------------------------------------------GET AVERAGE PRICES------------------------------------------------

def calculate_average_prices(df, quarters):
    #empty list to store the values
    avg_prices = []

    # Calculate average price for each city in each quarter
    for quarter in quarters:
        quarter_df = df[df['quarter'] == quarter]
        avg_price = quarter_df.groupby('city')['price_in_eur'].mean().reset_index()
        avg_price.rename(columns={'price_in_eur': f'price_in_eur_{quarter}'}, inplace=True)
        avg_prices.append(avg_price)

    # Merge all average price DataFrames on 'city'
    avg_price_comparison = avg_prices[0]
    for avg_price in avg_prices[1:]:
        avg_price_comparison = pd.merge(avg_price_comparison, avg_price, on='city')
    
    avg_price_comparison = pd.DataFrame(avg_price_comparison)

    return avg_price_comparison