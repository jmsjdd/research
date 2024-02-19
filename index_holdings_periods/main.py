import pandas as pd
import operating_systems.helper
import data_cleaning.manager
import data_analysis.calculations
import os

# Manual inputs
create_xlsx_to_get_prices = False
FILENAME_CONSTITUENT_WEIGHTS = "index_nzx50.csv"
PATH_TO_DATA_FOLDER = "C:\\Users\\JamesJudd\\Documents\\Data\\"

# Get paths
current_directory = os.getcwd()
# Get project name
current_file_path = os.path.abspath(__file__)
project_name = os.path.basename(os.path.dirname(current_file_path))
# Get directories
data_directory = f"{current_directory}\\{project_name}\\data\\"
constituent_weights_directory = f"{data_directory}{FILENAME_CONSTITUENT_WEIGHTS}"
venv_name = f".venv_{project_name}"
venv_directory = f"{current_directory}\\{project_name}\\{venv_name}\\"

# # Activate virtual environment
# venv_path = operating_systems.helper.find_folder_in_current_heirarchy(venv_name)
# if venv_path == None:
#     print("Cannot find venv path")
# else:
#     operating_systems.helper.activate_virtualenv()

# Clean data
df = data_cleaning.manager.clean_consituents(constituent_weights_directory)

# Create file to get prices
if create_xlsx_to_get_prices == True:
    data_cleaning.manager.create_xlsx_to_get_prices(
        df, data_directory, "nzx50_constituents_and_dates.csv"
    )


# Get cumulative returns from data frame with date, ID, weight (decimal format), return (decimal format)
nzx50 = data_analysis.calculations.cumulative_returns_from_constituents(
    df, "date", "weight", "return", "NZX 50"
)

# Graph the cumulative returns
data_analysis.calculations.graph_cumulative_returns(nzx50, "Growth of the NZX 50")
