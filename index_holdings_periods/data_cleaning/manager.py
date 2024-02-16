import pandas as pd
from datetime import datetime, timedelta


def run(path_to_data):
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
    df[["weight", "return"]] = df[["weight", "return"]] / 100

    return df
