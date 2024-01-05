"Github link: https://github.com/sulemanajaz/22033960_Data-and-Visualization"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from matplotlib.patches import Rectangle

def get_data_frames(filename, countries, indicator):
    # Read data using pandas into a dataframe.
    df = pd.read_csv(filename, skiprows=(4), index_col=False)
    # Get dataframe information.
    df.info()
    # To clean data, remove the unnamed column.
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # To filter data by countries.
    df = df.loc[df['Country Name'].isin(countries)]
    # To filter data by indicator code.
    df = df.loc[df['Indicator Code'].eq(indicator)]
    
    # Using melt function to convert all the years column into rows as one column.
    df2 = df.melt(id_vars=['Country Name','Country Code','Indicator Name',
                           'Indicator Code'], var_name='Years')
    # Deleting the country code column.
    del df2['Country Code']
    # Using pivot table function to convert countries from rows to separate 
    # columns for each country.   
    df2 = df2.pivot_table('value',['Years','Indicator Name','Indicator Code'],
                          'Country Name').reset_index()
    
    df_countries = df
    df_years = df2
    
    # Cleaning data by dropping nan values.
    df_countries.dropna()
    df_years.dropna()
    
    return df_countries, df_years

# List of countries
countries = ['Germany', 'Australia', 'United States', 'China', 'United Kingdom']

# Calling functions to get dataframes and use for plotting graphs.
df_c_agri, df_y_agri = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv', countries, 'AG.LND.AGRI.ZS')
df_c_pop, df_y_pop = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv', countries, 'SP.POP.GROW')
df_c_mort, df_y_mort = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv', countries, 'SH.DYN.MORT')
df_c_gdp, df_y_gdp = get_data_frames('API_NY.GDP.PCAP.KD.ZG_DS2_en_csv_v2_4748430.csv', countries, 'NY.GDP.PCAP.KD.ZG')

# Increase the size of the figures
fig = plt.figure(facecolor='Pink', figsize=(18, 10))
fig.suptitle('DOES CLIMATE EFFECT ON ECOSYSTEM?', fontsize=18, fontweight='bold')  # Make the title bold

# Create Bar Chart for Agricultural land (% of land area)
plt.subplot(2, 3, 1)
plt.bar(df_y_agri['Years'], df_y_agri[countries].T)
plt.title('Agricultural land (% of land area)')
plt.xlabel('Years', fontsize=6)  # Decrease the font size
plt.xticks(rotation=90, fontsize=5)  # Rotate x-axis labels and decrease font size
plt.ylabel('% of land area')

# Create Line plot for GDP per capita growth (annual %)
plt.subplot(2, 3, 2)
for country in countries:
    plt.plot(df_y_gdp['Years'], df_y_gdp[country], label=country)
plt.title('GDP per capita growth (annual %)')
plt.xlabel('Years', fontsize=6)  # Decrease the font size
plt.ylabel('Metric tons per capita')
plt.xticks(rotation=90, fontsize=5)  # Rotate x-axis labels and decrease font size

# Create Pie chart for Mortality rate, under-5 (per 1,000 live births)
plt.subplot(2, 3, 4)
mortality_list = [np.sum(df_y_mort[country]) for country in countries]
plt.pie(mortality_list, labels=countries, autopct='%1.1f%%')
plt.title('Mortality rate, under-5 (per 1,000 live births)')
plt.xlabel('Years', fontsize=6)  # Decrease the font size

# Create Bar Chart for Population growth (annual %)
plt.subplot(2, 3, 5)
for country in countries:
    plt.bar(df_y_pop['Years'], df_y_pop[country], label=country)
plt.title('Population growth (annual %)')
plt.xlabel('Years', fontsize=6)  # Decrease the font size
plt.ylabel('Population growth (annual %)')  # Add y-axis label
plt.legend()  # Add legend to differentiate countries
plt.xticks(rotation=90, fontsize=5)

# Define the cream color in RGB
cream_rgb = (255/255, 253/255, 208/255)

# Add a paragraph on the right side of the dashboard with a cream color box
paragraph_title1 = "Student Name: Suleman Ajaz "
paragraph_title = "Student Id: 22033960"
paragraph = ("This dashboard titled 'DOES CLIMATE EFFECT ON ECOSYSTEM?'\n\n"
            "provides a comprehensive view of various factors influenced\n\n"
            "by climate such as land use, population, mortality, and GDP.\n\n"
            "1) Agricultural Land: The bar graph shows a consistent growth\n\n" 
            "in the percentage of agricultural land over the years,\n\n"
            "indicating an expansion in farming activities.\n\n"
             "2) Population Growth: The pie chart reveals that\n\n"
             "China has experienced the most significant\n\n" 
             "population growth at 54.4%, followed by the United States at 23.2%.\n\n"
             "Explanation:\n"
             "China: 113% increase in 30 years.\n"
             "United States: 72.9% increase in 30 years.\n"
             "Australia: 34.5% increase in 30 years.\n"
             "Germany: 30% increase in 30 years.\n"
             "United Kingdom: 20% increase in 30 years.\n\n"
             "3) Infant Mortality Rate: The second pie chart highlights\n\n"
             "the U.S. as having the highest infant mortality rate at\n\n" 
             "49.2% among the five countries displayed.\n\n"
             "Explanation:\n"
             "All countries shown have experienced a decrease in\n\n"
             "mortality rates over the past few decades.\n"
             "China has the lowest mortality rate, at around 4 per 1,000 live births.\n"
             "The United States has the highest mortality rate, at around 10 per 1,000 live births.\n\n"
             "4) GDP per Capita Growth: The line graph depicts the\n\n" 
             "fluctuating GDP per capita growth for each country,\n\n"
             "with no clear pattern of consistent growth or decline.\n\n"
             "Explanation:\n"
             "All countries shown have experienced positive GDP per\n\n"
             "capita growth over the past few decades.\n\n"
             "China has the highest GDP per capita growth, at around 20% per year.\n"
             "The United Kingdom has the lowest GDP per capita growth, at around 0% per year.")

# Define the rectangle for the box
rect = Rectangle((0.63, 0.1), 0.35, 0.8, linewidth=1, edgecolor='black', facecolor=cream_rgb, transform=fig.transFigure)

# Add the paragraph title inside the box
plt.figtext(0.76, 0.94, paragraph_title1, ha='left', va='center', fontsize=12, color='black', fontweight='bold')
# Add the paragraph title inside the box
plt.figtext(0.76, 0.92, paragraph_title, ha='left', va='center', fontsize=12, color='black', fontweight='bold')
# Add the rectangle to the figure
fig.patches.append(rect)

# Add text inside the box
plt.figtext(0.65, 0.53, paragraph, ha='left', va='center', fontsize=9, color='black')
plt.tight_layout(rect=[0, 0, 0.95, 1])  # Adjust layout to avoid title overlap
plt.savefig("22033960.png",dpi=300)
