"""Weather Visuals - Samantha Song - 2025.03.03"""
# Data from UN - http://data.un.org/Data.aspx?d=GHG&f=seriesID%3aCO2

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
FILE_NAME = 'UNdata_Export_20250303_182435311.csv'
data = pd.read_csv(FILE_NAME)
FOLDER = 'Weather Plots/'

# Seperate into top 6 Countries and others
C_NUM = 10
top_count = data[data['Year'] == 2020].sort_values('Value',
                                                   ascending=False).head(C_NUM)['Country or Area']
data['Country or Area (Mine)'] = data['Country or Area']
data.loc[~data['Country or Area (Mine)'].isin(top_count), 'Country or Area (Mine)'] = 'Other'

scatterplot = sns.boxplot(data, x='Year', y='Value')
scatterplot.tick_params(axis='x', rotation=90)
scatterplot.set_title('Yearly CO2 Emissions by Country')
scatterplot.set_xlabel('Country')
scatterplot.set_ylabel('Yearly CO2 Emissions')
plt.show()

histogram = sns.histplot(data, x='Country or Area (Mine)', weights='Value')
histogram.tick_params(axis='x', rotation=90)
histogram.set_title('Total CO2 Emissions by Country (from 1990 to 2021)')
histogram.set_xlabel('Country')
histogram.set_ylabel('Total CO2 Emissions')
plt.show()

by_year_hist = sns.histplot(data, x='Year', weights='Value', bins=32,
                            hue='Country or Area (Mine)', multiple='stack',
                            palette=sns.color_palette('Spectral', n_colors=C_NUM+1))
by_year_hist.tick_params(axis='x', rotation=90)
by_year_hist.set_title('Total CO2 Emissions by Year (from 1990 to 2021)')
by_year_hist.set_xlabel('Year')
by_year_hist.set_ylabel('Total CO2 Emissions')
plt.show()
