import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Import data
df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Data')

    # Create first line of best fit (1880 - 2050)
    slope1, intercept1, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(1880, 2051)
    y1 = slope1 * x1 + intercept1
    plt.plot(x1, y1, color='r', label='Best fit line (1880-2050)')

    # Create second line of best fit (2000 - 2050)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000, 2051)
    y2 = slope2 * x2 + intercept2
    plt.plot(x2, y2, color='g', label='Best fit line (2000-2050)')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save and return the plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()