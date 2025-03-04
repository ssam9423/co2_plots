"""Weather Visuals - Samantha Song - 2025.03.03"""
# Data from UN - http://data.un.org/Data.aspx?d=GHG&f=seriesID%3aCO2

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
FILE_NAME = 'UNdata_Export_20250303_182435311.csv'
FOLDER = 'Visuals - Data Visualization/'
IMG_FOLDER = 'Weather Plots/'
data = pd.read_csv(FOLDER + FILE_NAME)

# Seperate into top 6 Countries and others
C_NUM = 10
top_count = data[data['Year'] == 2020].sort_values('Value',
                                                   ascending=False).head(C_NUM)['Country or Area']
data['Country or Area (Mine)'] = data['Country or Area']
data.loc[~data['Country or Area (Mine)'].isin(top_count), 'Country or Area (Mine)'] = 'Other'

# Yearly CO2 Emissions from top 10 countries
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7, 4), width_ratios=[3,1])
fig.delaxes(axes[1])
scatterplot = sns.lineplot(data[data['Country or Area'].isin(top_count)], x='Year', y='Value',
                           hue='Country or Area', style='Country or Area')
sns.move_legend(scatterplot, "upper left", bbox_to_anchor=(1, 1))
fig.suptitle('Yearly CO2 Emissions (Top ' + str(C_NUM) + ' Countries)')
scatterplot.set_xlabel('Year')
scatterplot.set_ylabel('Yearly CO2 Emissions')
graph_name = 'Yearly CO2 Emissions'
plt.savefig(FOLDER + IMG_FOLDER + graph_name)
plt.show()

# Total Emissions by Country from 1990 - 2021
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(7, 5), height_ratios=[8,1])
fig.delaxes(axes[1])
histogram = sns.histplot(data, x='Country or Area (Mine)', weights='Value',
                         hue='Country or Area (Mine)',
                         palette=sns.color_palette('Spectral', n_colors=C_NUM+1),
                         ax=axes[0])
histogram.set_title('Total CO2 Emissions by Country (from 1990 to 2021)')
histogram.set(xticklabels=[])
histogram.set(xlabel=None)
sns.move_legend(histogram, "lower center", bbox_to_anchor=(.5, -0.35),
                ncol=3, title=None, frameon=False,)
histogram.set_ylabel('Total CO2 Emissions')
graph_name = 'Total CO2 Emissions by Country'
plt.savefig(FOLDER + IMG_FOLDER + graph_name)
plt.show()

# Total CO2 Emissions by Year
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7, 4), width_ratios=[3,1])
fig.delaxes(axes[1])
by_year_hist = sns.histplot(data, x='Year', weights='Value', bins=32,
                            hue='Country or Area (Mine)', multiple='stack',
                            palette=sns.color_palette('Spectral', n_colors=C_NUM+1),
                            ax=axes[0])
sns.move_legend(by_year_hist, "upper left", bbox_to_anchor=(1, 1))
fig.suptitle('Total CO2 Emissions by Year (from 1990 to 2021)')
by_year_hist.set_xlabel('Year')
by_year_hist.set_ylabel('Total CO2 Emissions')
graph_name = 'Total CO2 Emissions by Year'
plt.savefig(FOLDER + IMG_FOLDER + graph_name)
plt.show()
