import pandas as pd


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


def merge_data_frames(df_list):
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
    
    #concatenate the dataframes
    final_dataframe = pd.concat(dataframes_merged, ignore_index=True)
    return final_dataframe
