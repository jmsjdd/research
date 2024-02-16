import pandas as pd
import operating_systems.functions
import data_cleaning.manager
import data_analysis.calculations
import os

# Manual inputs
PATH_TO_DATA = "C:\\Users\\JamesJudd\\Documents\\Data\\index_nzx50.csv"

# Get current folder name
file_path = os.path.abspath(__file__)
# Extract the directory name (folder name) from the file path
project_name = os.path.basename(os.path.dirname(file_path))

venv_name = f'.venv_{project_name}'
print(venv_name)
current_folder = os.os.path.basename(os.getcwd())
current_dir = os.path.dirname(os.path.abspath(__file__))
print(os.listdir(current_dir))
# Activate virtual environment
venv_path = operating_systems.functions.find_folder_in_current_heirarchy(venv_name)
if venv_path == None:
    print("Cannot find venv path")
else:
    operating_systems.functions.activate_virtualenv()

# Clean data
df = data_cleaning.manager.run(PATH_TO_DATA)

# Get cumulative returns from data frame with date, ID, weight (decimal format), return (decimal format)
nzx50 = data_analysis.calculations.cumulative_returns_from_constituents(
    df, "date", "weight", "return", "NZX 50"
)

# Graph the cumulative returns
data_analysis.calculations.graph_cumulative_returns(nzx50, "Growth of the NZX 50")
