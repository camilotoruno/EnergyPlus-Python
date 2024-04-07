import ep_res_aggregation

drybulb_temp = 'Environment:Site Outdoor Air Drybulb Temperature [C](Hourly)'
wetbulb_temp = 'Environment:Site Outdoor Air Wetbulb Temperature [C](Hourly)'

arguments = {
    # energy plus arguments 
    "simulation_res_fldr": "/Users/camilotoruno/Documents/local_research_data/simulations_LA_Detroit",
    "options": {"columns_to_average": [drybulb_temp, wetbulb_temp], 
            "unchanged_columns": ['Date', 'Month', 'Day'], 
            "results_file": "output_file.csv",
            },
    # "eplusout_exclude_header_key": [""]

    # energy pricing arguments
    "energy_pricing": "/some/folder/of/data",

    # metadata argumets 
    "reference_buildstock": "/Users/camilotoruno/Documents/local_research_data/buildings_LA_Detroit/buildstock.csv",
    "metadata_choices": "metadata_choices.csv",
    }

ep_res_aggregation.run(arguments)