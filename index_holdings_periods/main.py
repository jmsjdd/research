import pandas as pd
import operating_systems.helper
from data_cleaning import data_cleaning_manager, file_creation
from data_analysis.manipulations import manipulations_manager
from data_analysis.graph import graph_helpers
import data_analysis.calculations
import os

# Manual inputs
create_xlsx_to_get_prices = False
FILENAME_CONSTITUENT_WEIGHTS = "index_nzx50.csv"
FILENAME_CONSTITUENT_PRICING = "index_history_pricing.xlsx"
PERIODS_TO_TEST = [1, 6, 12, 24, 36, 60, 120]
# PATH_TO_DATA_FOLDER = "C:\\Python\\research\\index_holdings_periods\\data\\"

# Get paths
current_directory = os.getcwd()
# Get project name
current_file_path = os.path.abspath(__file__)
project_name = os.path.basename(os.path.dirname(current_file_path))
# Get directories
data_directory = f"{current_directory}\\{project_name}\\data\\"
constituent_weights_directory = f"{data_directory}{FILENAME_CONSTITUENT_WEIGHTS}"
constituent_pricing_directory = f"{data_directory}{FILENAME_CONSTITUENT_PRICING}"
venv_name = f".venv_{project_name}"
venv_directory = f"{current_directory}\\{project_name}\\{venv_name}\\"

# # Activate virtual environment
# venv_path = operating_systems.helper.find_folder_in_current_heirarchy(venv_name)
# if venv_path == None:
#     print("Cannot find venv path")
# else:
#     operating_systems.helper.activate_virtualenv()

# Clean data
df_weights, df_prices = data_cleaning_manager.run(
    constituent_weights_directory, constituent_pricing_directory
)

# Create file to get prices
if create_xlsx_to_get_prices == True:
    file_creation(df_weights, data_directory, "nzx50_constituents_for_bb.xlsx")

# Get adjusted, weighted ctr of consituents for different periods
df = manipulations_manager.full_index_constituents_data(
    df_weights, df_prices, PERIODS_TO_TEST
)

# Group to index returns and cumulate
df_index_returns = manipulations_manager.index_returns(df, PERIODS_TO_TEST)
print(df_index_returns)

# Graph
graph_helpers.plot_line_graph(df_index_returns, PERIODS_TO_TEST)
