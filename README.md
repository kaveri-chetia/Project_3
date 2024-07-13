# :hotel: Inside Airbnb

We are a consultancy firm dedicated to maximizing your rental income through expert Airbnb management, market analysis, and strategic pricing.


# Project Overview
The project highlights the impact of Airbnb on residential communities.  We have compiled comprehensive quarterly data on Airbnb rentals, segmented by major cities worldwide. This includes detailed information on average income, pricing, listings, and reviews.
We aim to use this data to answer key business questions about Airbnb market economy.

# Problem Statement

Today's short-term rental market in the biggest cities in Europe  is very saturated. As a new investor/potential property owner, it is important to understand the current market situation and demand/offer to make informed decisions. To address this problem there is a need to explore the current price and location trends, as well as look into guest experience enhancement opportunities and to evaluate the impact regulations have on the short term rental market. 

### Example beneficiaries of this data analysis include:  
As an investor, I would like to know which neighborhood has the most potential for revenue growth.  
As a government agency, we would like to research which regions offer regulatory policy in the short term property market. 
As a tourism agency, we would like to create marketing strategies to promote destinations based on popular Airbnb locations and trends.   

## :question:`Business Questions
The business questions will help us uncover insights that address the problem statement and provide analysis based on Inside Airbnb’s available datasets.

1.How many listings in each city?
2.How are these listings distributed within the city?
3.How the distribution of room types differs significantly between neighbourhoods.
4.Comparative study of Top 10 popular neighbourhoodsof each city.
5.What is the price distribution in each city?
6.What is the average/max/min price in each city?
7.How do the cities compare?
8.What are the price trends over the last four quarters?
9.Are there differences in amount of listings/price between regulated (e.g. Berlin, Barcelona) and unregulated (Prague, Vienna) cities?

### **EDA - 1️⃣ Hypothesis**

**Variables used:**

- cities;
- neighbourhood;
- room_types.


![Data Visualization](EDA/EDA_visualizations/Countplot1.png)
*Comparison of top 10 neighborhoods of 6 cities on the basis of listings*

![Data Visualization](EDA/EDA_visualizations/Stackedplot1.png)
*Comparison of top room-types of 6 cities*



  
## :goal_net: Goals
1. Answer all business questions using datasets of 6 different cities.
2. Provide statistical analysis to visualize key business questions.

## Scope
Top 6 EU cities by population (Paris, London, Madrid, Barcelona, Istanbul and Rome). 

## Milestones
1.Project Preparation
  Organize the project team
  Create Kanban board
2.Define problem statement
  Identify Business Questions
3.Code Review and Testing
  Review code from Local and Dev branches. 
  Once reviewed and approved, merge into Main branch.  
4.Presentation
  Prepare presentation

## :toolbox: Tools and Technologies Used

- Python: The main programming language used for data processing, analysis, and visualization.
- Jupyter Notebook: Used for data cleaning, merging datasets, estimating the adoption curve, and addressing the project questions.
- Plotly python graphing library

## Project Structure

The project structure is as follows:

- `notebooks/main.py`: The Jupyter Notebook containing the data processing, analysis, and visualization code.
- `data/`: A folder containing the dataset files obtained from the IEA.
- `app/`: A folder containing the application code for creating the project dashboard.
- `requirements.txt`: A file specifying the dependencies required to run the project.

##

## Conclusion

This data project provides insights on-

1.Average prices are higher in cities with higher cost of living index.

2.To conclude the price patterns regarding summer/winter periods, more data is needed.

3.The listings are concentrated in touristic locations and by the airport, which shows 
  that there is demand for these locations in particular. 

### Link
(https://insideairbnb.com/get-the-data/and)
  

