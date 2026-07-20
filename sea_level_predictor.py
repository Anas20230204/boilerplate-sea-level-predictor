import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    the_linregress = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = the_linregress.slope
    intercept = the_linregress.intercept

    list_comp = [int(x) for x in range(1880, 2051)]
    list_comp = pd.Series(list_comp)

    formula = (slope * list_comp) + intercept
    plt.plot(list_comp, formula, color='red')

    # Create second line of best fit
    subdf = df.loc[df['Year'] >= 2000]

    new_regress = linregress(subdf['Year'], subdf['CSIRO Adjusted Sea Level'])
    new_slope = new_regress.slope
    new_intercept = new_regress.intercept

    list_comp2 = [int(x) for x in range(2000, 2051)]
    list_comp2 = pd.Series(list_comp2)

    height = (new_slope * list_comp2) + new_intercept
    plt.plot(list_comp2, height, color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (Required by freeCodeCamp)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
