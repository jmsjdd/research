import pandas as pd


# Manual inputs
PATH_TO_DATA = "C:\\Users\\JamesJudd\\Documents\\Data\\index_nzx50.csv"


# Collect data
df = pd.read_csv(PATH_TO_DATA)

# Add dates

print(len(df.columns))

for col_index in range(len(df.columns)):
    col_name = df.columns[col_index]
    if "Unnamed" not in col_name:
        df.iloc[0, col_index + 1] = "weight"
        df.iloc[0, col_index + 2] = "return"
        df[col_index + 3].fillna(col_name, inplace=True)
        df.iloc[0, col_index + 3] = "date"


print(df)
