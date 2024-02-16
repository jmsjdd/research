import pandas as pd
import data_cleaning.manager
import data_analysis.calculations

# Manual inputs
PATH_TO_DATA = "C:\\Users\\JamesJudd\\Documents\\Data\\index_nzx50.csv"

df = data_cleaning.manager.run(PATH_TO_DATA)

nzx50 = data_analysis.calculations.cumulative_returns_from_constituents(
    df, "date", "weight", "return", "NZX 50"
)

data_analysis.calculations.graph_cumulative_returns(nzx50)
