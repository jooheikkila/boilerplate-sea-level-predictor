import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')

    # Create first line of best fit
    line_first = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_all = pd.Series(range(1880, 2050))
    sea_levels_predicted = line_first.slope * years_all + line_first.intercept

    plt.plot(years_all, sea_levels_predicted, 'red', label='Fit: 1880–2050')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    line_second = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    years_recent = pd.Series(range(2000, 2050))
    sea_levels_recent = line_second.slope * years_recent + line_second.intercept

    plt.plot(years_recent, sea_levels_recent, 'green', label='Fit: 2000–2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()