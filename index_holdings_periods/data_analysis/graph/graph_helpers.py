import matplotlib.pyplot as plt

# import seaborn as sns


def plot_line_graph(df, list_of_periods, title):
    """
    Create a line graph for the DataFrame with columns specified in list_of_periods and the 'date' column.

    Parameters:
    - df: DataFrame containing the data with the 'date' column and columns specified in list_of_periods.
    - list_of_periods: List of column names to be plotted.

    Example:
    plot_line_graph(df, ['1 month rebalancing cumulation', '6 month rebalancing cumulation', ...])
    """
    # Plot the data
    plt.figure(figsize=(10, 6))  # Adjust figure size if needed
    for period in list_of_periods:
        col_name = f"{period} month rebalancing cumulation"
        plt.plot(df["date"], df[col_name], label=period)

    # Add labels and title
    plt.xlabel("Date")
    plt.ylabel("Cumulative Returns")
    plt.title(title)
    plt.legend(loc="upper left")  # Adjust legend location if needed
    plt.grid(True)

    # Automatically adjust axis limits to fit the data
    plt.autoscale()

    # Show the plot
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()
