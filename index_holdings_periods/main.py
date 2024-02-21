import pandas as pd
import operating_systems.helper
from data_cleaning import data_cleaning_manager, file_creation
from data_analysis.graph import graph_helpers
from data_analysis.portfolio_build import portfolio_build_manager
from data_analysis.returns import returns_helpers
from data_analysis.index_aggregation import index_aggregation_manager
import os

# Manual inputs
create_xlsx_to_get_prices = False
FILENAME_CONSTITUENT_WEIGHTS = "index_nzx50.csv"
FILENAME_CONSTITUENT_PRICING = "index_history_pricing.xlsx"
PERIODS_TO_TEST = [1, 3, 6, 12, 24, 120]
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
df_weights, df_prices, df_all = data_cleaning_manager.run(
    constituent_weights_directory, constituent_pricing_directory
)
print("Data cleaned")

# Create file to get prices
if create_xlsx_to_get_prices == True:
    file_creation(df_weights, data_directory, "nzx50_constituents_for_bb.xlsx")

# Add returns
returns_helpers.monthly_constituent_returns(df_all)

# Build portfolios for each period
portfolio_build_manager.run(df_all, PERIODS_TO_TEST)
print("Portfolios built")

# Aggregate constituents into single portfolio
df_index, df_index_same_start_dt = index_aggregation_manager.run(
    df_all, PERIODS_TO_TEST
)

# Add cumulate returns
df_index = returns_helpers.cumulate_returns(df_index, PERIODS_TO_TEST)
df_index_same_start_dt = returns_helpers.cumulate_returns(
    df_index_same_start_dt, PERIODS_TO_TEST
)
print("Data aggregated and cumulative returns added")

# Graph
graph_helpers.plot_line_graph(df_index, PERIODS_TO_TEST, "Cumulative returns")
graph_helpers.plot_line_graph(
    df_index_same_start_dt,
    PERIODS_TO_TEST,
    "Cumulative returns with the same start date",
)

# df_index_returns.to_excel(
#     "C:\\Python\\research\\index_holdings_periods\\data\\output2.xlsx", index=False
# )
# TODO
"""
Limitation: currently does not re-distribute de-list company funds and underweights investments afterwards

"""
