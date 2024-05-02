import ep_res_aggregation

drybulb_temp = 'Environment:Site Outdoor Air Drybulb Temperature [C](Monthly)'
wetbulb_temp = 'Environment:Site Outdoor Air Wetbulb Temperature [C](Monthly)'

arguments = {
    # energy plus arguments 
    "simulation_res_fldr": "/Users/camilotoruno/Documents/local_research_data/simulations_five_cities",
    "options": {"columns_to_average": [drybulb_temp, wetbulb_temp], 
            "unchanged_columns": ['Date', 'Month', 'Day', 'Date/Time'], 
            "results_file": "results_summary.csv",
            },
    "overwrite": True, 
    }

ep_res_aggregation.run(arguments)