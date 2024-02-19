import pandas as pd


def create_xlsx_to_get_prices(df, path_to_save_data, filename):
    """
    Creates an xlsx file to load to BB to get price data
    """

    path = f"{path_to_save_data}{filename}"

    # Create a duplicate DataFrame
    df_duplicate = df.copy()

    # Columns to drop
    columns_to_drop = ["weight", "return", "date"]

    # Drop columns
    df_duplicate.drop(columns=columns_to_drop, inplace=True)

    # Sort values by "ID"
    df_duplicate.sort_values(by="ID", inplace=True)

    # Remove duplicate rows
    df_cleaned = df_duplicate.drop_duplicates()

    # Add a blank row after each existing row
    result = pd.concat(
        [
            df_cleaned,
            pd.DataFrame(index=df_cleaned.index, columns=df_cleaned.columns),
        ],
        axis=0,
    ).sort_index(kind="merge")

    # Transpose DataFrame
    transposed_df = result.transpose()

    # Save the transposed DataFrame to an Excel file without including the index
    transposed_df.to_excel(
        path,
        index=False,  # Set index=False to exclude index column
    )
