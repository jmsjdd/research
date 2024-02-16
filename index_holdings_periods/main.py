import pandas as pd
from datetime import datetime, timedelta
import data_cleaning.manager

# Manual inputs
PATH_TO_DATA = "C:\\Users\\JamesJudd\\Documents\\Data\\index_nzx50.csv"

df = data_cleaning.manager.run(PATH_TO_DATA)

print(df)
