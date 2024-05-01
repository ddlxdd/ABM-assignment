import mesa
from model import VirusOnNetwork
from mesa import batch_run
import pandas as pd



parameters = {
    "num_nodes": range(10, 100, 20),
    "initial_outbreak_size": [1, 5, 10],
    "virus_spread_chance": [0.2, 0.4, 0.6],
    "recovery_chance": [0.1, 0.3, 0.5],
    "superspreader_chance": [0.01, 0.05, 0.1]
}


result = batch_run(
    VirusOnNetwork,
    parameters,
    iterations=3,
    max_steps=50,
    
    #model_reporters={
        #"Infected": lambda m: m.datacollector.get_model_vars_dataframe()["Infected"].iloc[-1],
        #"Susceptible": lambda m: m.datacollector.get_model_vars_dataframe()["Susceptible"].iloc[-1],
        #"Resistant": lambda m: m.datacollector.get_model_vars_dataframe()["Resistant"].iloc[-1]
    #}
    
)

result.run_all()

pd.Datafram(result).to_csv("batch_run_results.csv")
