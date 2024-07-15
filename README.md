# EnergyPlus Python Simulation Pipeline

## script_epwork.py Setup:
This is the main workflow script. Use it to run a large job for building energy simulations. Define the parameters of the simulation in the file (e.g. list of cities and climate scenarios to run the simulation for). Then run the program either from an IDE or terminal. 

## eprun_s.py Example usage: 
This is the core functionality which is orchestrated by script_epwork.py. There's no need to directly call it, however it can be called directly from the command line. 

## run_output_aggregation.py
Use script to aggregate output from simulation results folder. This is currently set up for to monthly data, however you may need to change the data to aggregate truly monthly data. Changing the reporting frequency changes the column header changes (e.g. Date/Time, Date), and thus this will need to be modified lighly for different frequencies. Keep in mind the design of the aggregation script to read and write single lines (rather than loading the full output file) to avoid loading the entire aggregated csv in memory (because it could be larger than memory for sample size datasets). 

## pricing_data_cleaning.ipynb
Use this to clean up EIA / FRED electriicty, natural gas, etc pricing data and format it for the next step, calculating household costs. Prior formatted / cleaned data is held in ```seas-mtcraig/data_sharing/Energy Burdens Under Climate Change/Energy rates```

## joining_metadata_calculating_costs.ipynb
Use to join the metadata (buildstock.csv) data on the aggregated results, calculate household level costs. 