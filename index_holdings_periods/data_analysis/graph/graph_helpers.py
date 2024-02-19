import matplotlib.pyplot as plt
import seaborn as sns


def graph_cumulative_returns(df, list_of_periods):
    """
    Generate a line graph of cumulative returns.

    :param df: DataFrame with date in the first column and cumulative returns in subsequent columns.
    :param title: Title of the graph.
    """
    # Set the style using Seaborn
    sns.set(style="whitegrid")

    # Get the column names excluding the first column (date column)
    columns_to_plot = df.columns[1:]

    # Create a new figure and axis
    plt.figure(figsize=(12, 8))
    ax = plt.subplot(111)

    # Use a color palette with distinct colors for each line
    colors = sns.color_palette("husl", len(columns_to_plot))

    # Iterate over each column and plot the line on the same axis
    for i, column in enumerate(columns_to_plot):
        ax.plot(df["date"], df[column], label=column, color=colors[i % len(colors)])

    # Set labels and title with nicer fonts
    plt.xlabel("Date", fontsize=14, fontname="Arial")
    plt.ylabel("Cumulative Returns", fontsize=14, fontname="Arial")
    plt.title(title, fontsize=16, fontweight="bold", fontname="Arial")
    plt.xticks(fontsize=12, fontname="Arial", rotation=45)
    plt.yticks(fontsize=12, fontname="Arial")

    # Add legend outside the plot
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=12)

    # Tight layout to prevent overlapping labels
    plt.tight_layout()

    # Show the plot
    plt.show()
