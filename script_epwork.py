import eprun_s
import multiprocessing
import os 

#TODO Simulation output configuration settings 
    # in reset_idf_schedules_path.set_EnergyPlus_Simulation_Output 
        # if no configuration file provided: print no config file provided, using existing IDF file simulation output arguments 
        # if configuration file provided 
            # if configuration file does not exists raise RuntimeError()

            # load the configuration file as provided 

            # for each IDF
                # open the IDF 
                # for each parameter in the config file 
                    # if the paramter exists set its values 
                        # if the parameters match 
                            # overwrite the original with new args 
                        # else 
                            # make new IDF object attribute 
                # save the IDF


if __name__ == '__main__':
    multiprocessing.freeze_support()        # required to prevent issues for multicore processing in run_energyplus_simulations() 

    arguments = {
        'cities': ['Detroit', 'Los Angeles'], 
        # 'cities': ['Dallas', 'Philadelphia'],
        'climate_scenarios': ["historical_1980-2020", "rcp45cooler_2020-2060"],
        }

    run_args = {

        'weather_folder': '/Volumes/seas-mtcraig/EPWFromTGW/TGWEPWs',
        # 'weather_folder': '/Users/camilotoruno/Documents/GitHub/EnergyPlus-Python/TGWEPWs_trimmed',

        # 'buildings_folder': '/Users/camilotoruno/Documents/GitHub/EnergyPlus-Python/Buildings',
        'buildings_folder': '/Users/camilotoruno/Documents/local_research_data/bldgs_idf_output_flags',

        'output_folder': '/Users/camilotoruno/Documents/local_research_data/sims_LA_Detroit',
        # 'output_folder': 'Volumes/seas-mtcraig/ctoruno/Buildings_Dallas_downsample_simulations',
        # 'output_folder': '/Users/camilotoruno/Documents/GitHub/EnergyPlus-Python/simulations',

        'overwrite_output': True, 
        'verbose': True,
        "max_cpu_load": 0.7,       # must be in the range [0, 1]. The value 1 indidcates all CPU cores, 0 indicates 1 CPU core

        'ep_install_path': '/Applications/OpenStudio-3.4.0/EnergyPlus',


        # Define the desired simulation settings 
        #############  required if setting IDF file requested outputs here rather than in upstream 
        'ResStockToEnergyPlus_repository': '/Users/camilotoruno/Documents/GitHub/building_energy_modeling',         
        'pathnameto_eppy': "/Users/camilotoruno/anaconda3/envs/research/lib/python3.11/site-packages/eppy",
        "iddfile": "/Applications/OpenStudio-3.4.0/EnergyPlus/Energy+.idd",
        'idf_configuration': "/Users/camilotoruno/Documents/GitHub/EnergyPlus-Python/simulation_output_configuration.idf",      # output settings configuration
        ############
        }


    ################################## RUN SMULATIONS ############################################

    sim = 1
    total_sims = len(arguments['climate_scenarios']) * len(arguments['cities'])
    for scenario in arguments['climate_scenarios']:
        for city in arguments['cities']:
            print(f"Run \t City \t\t\t Scenario")
            print(f"{sim}/{total_sims} \t {city} \t\t {scenario}")
            run_args['city'] = city
            run_args['climate'] = scenario
            eprun_s.run_energyplus_simulations(**run_args)
            sim += 1
            print("\n\n")
