import pandas as pd
from datetime import datetime
from . import data_cleaning_utils


def constituent_weights(path_to_data):
    """
    Parse constituent weight data from CSV file.

    Parameters:
    - path_to_data (str): Path to the CSV file containing constituent weight data.

    Returns:
    - df (DataFrame): Parsed DataFrame containing constituent weight data.
    """
    # Collect data
    df = pd.read_csv(path_to_data)
    df = df.astype(str)

    # Add column names
    for col_index in range(len(df.columns)):
        col_name = df.columns[col_index]
        if "Unnamed" not in col_name:
            df.iloc[0, col_index + 1] = "weight"
            df.iloc[0, col_index + 2] = "return"
            df.iloc[:, col_index + 3] = col_name
            df.iloc[0, col_index + 3] = "date"

    # Create an empty DataFrame to store the final result
    result_df = pd.DataFrame(columns=["date", "ID", "weight", "return"])

    # Iterate over the columns of the original DataFrame
    for i in range(0, len(df.columns), 4):
        # Extract the date from the first row of each set of 4 columns
        date = df.iloc[0, i + 3]

        # Extract the data for each date
        temp_df = pd.DataFrame(
            {
                "ID": df.iloc[1:, i],
                "weight": df.iloc[1:, i + 1],
                "return": df.iloc[1:, i + 2],
                "date": df.iloc[1:, i + 3],
            }
        )

        # Append the extracted data to the result DataFrame
        result_df = pd.concat([result_df, temp_df], ignore_index=True)

    del df

    df = result_df

    del result_df

    # Make date column datetime
    df["date"] = df["date"].apply(
        lambda x: datetime.fromordinal(datetime(1899, 12, 30).toordinal() + int(x) - 2)
    )

    # Divide percentages by 100
    df[["weight", "return"]] = df[["weight", "return"]].astype(float)
    df[["weight"]] = df[["weight"]] / 100

    # Make date end of month
    df["date"] = df["date"].apply(data_cleaning_utils.end_of_month)

    return df


def constituent_pricing(path_to_data):
    """
    Parse constituent pricing data from Excel file.

    Parameters:
    - path_to_data (str): Path to the Excel file containing constituent pricing data.

    Returns:
    - df (DataFrame): Parsed DataFrame containing constituent pricing data.
    """
    # Collect data
    df = pd.read_excel(path_to_data)
    df = df.astype(str)

    # Create an empty DataFrame to store the final result
    result_df = pd.DataFrame(columns=["ID", "date", "price_t"])

    # Iterate over the columns of the original DataFrame
    for i in range(0, len(df.columns), 2):
        # # Extract the date from the first row of each set of 4 columns
        # date = df.iloc[0, i + 3]

        # Extract the data for each date
        temp_df = pd.DataFrame(
            {
                "ID": df.columns[i],
                "date": df.iloc[:, i],
                "price_t": df.iloc[:, i + 1],
            }
        )

        # Append the extracted data to the result DataFrame
        result_df = pd.concat([result_df, temp_df], ignore_index=True)

    del df

    # Make price column float and remove blank rows
    result_df["price_t"] = result_df["price_t"].astype(float)
    result_df.loc[:, "price_t"] = result_df["price_t"].replace("", float("nan"))
    df = result_df.dropna(subset=["price_t"])

    del result_df

    # Convert the float column to int
    df["date"] = df["date"].astype(float).round().astype(int)

    # Make date column datetime
    df["date"] = df["date"].apply(
        lambda x: datetime.fromordinal(datetime(1899, 12, 30).toordinal() + int(x) - 2)
    )

    # Make date end of month
    df["date"] = df["date"].apply(data_cleaning_utils.end_of_month)

    return df
