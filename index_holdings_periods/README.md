# Overview

This package is for creating a pdf report

# Installation

Save and run in your c drive, not under the user. You will not have permission to create/delete folders under any users.

'''bash to create environment
    cd research\index_holdings_periods
    cd index_holdings_periods
    python -m venv .venv_index_holdings_periods
    .\.venv_index_holdings_periods\Scripts\activate
    pip install -r requirements.txt
'''

'''bash to open existing environment when another venv is open
    deactivate
    cd ..
'''

...bash to save requirements - delete the old file first
    pip freeze > requirements.txt
...

# Environmental Variables

Create a .env file (make sure .env is included in the .gitignore)
Get the following variables from Dashlane:
.env - Azure

# How it works

1) Data is loaded to a data frame from sharepoint - uses functions>>sharepoint
2) Graph is produced using functions>>other
3) Graphs are saved in the report compiler folder.
4) A Tex file turns the graphs into a report.
5) The report is saved in the output folder.
