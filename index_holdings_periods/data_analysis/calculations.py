import pandas as pd
import matplotlib.pyplot as plt


def cumulative_returns_from_constituents(
    data_frame, date_col_name, weight_col_name, return_col_name, portfolio_name
):
    """
    Calcs cumulative returns from constituents. Renames the cumulative returns column to the portfolio name.
    """

    # Calc weighted return
    data_frame["weighted_return"] = (
        data_frame[weight_col_name] * data_frame[return_col_name]
    )

    # Group by date
    df_grouped = (
        data_frame.groupby(date_col_name)["weighted_return"].sum().reset_index()
    )

    # Rename
    df_grouped.rename(columns={"weighted_return": return_col_name}, inplace=True)

    # Calc cumulative return
    df_grouped[portfolio_name] = df_grouped["return"].cumsum()

    # Drop return col to keep data clean
    df_grouped.drop(columns=["return"], inplace=True)

    return df_grouped


def graph_cumulative_returns(df):
    """
    Have date in first col and cumulative returns in each col following with the portfolio name as the cumulative returns col name.
    """
    # Get the column names excluding the first column (date column)
    columns_to_plot = df.columns[1:]

    # Create a new figure and axis
    plt.figure(figsize=(10, 6))
    ax = plt.subplot(111)

    # Iterate over each column and plot the line on the same axis
    for column in columns_to_plot:
        ax.plot(df["date"], df[column], label=column)

    # Set labels and title
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Overlay Line Graph")
    plt.legend()

    # Show the plot
    plt.show()
