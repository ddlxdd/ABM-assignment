import mesa
from model import VirusOnNetwork
from mesa.batchrunner import batch_run
import pandas as pd


def main():
    parameters = {
        "num_nodes": 3,
        "avg_node_degree": 4,
        "initial_outbreak_size": 10,
        "virus_spread_chance": 0.4,
        "recovery_chance": 0.3,
        "superspreader_chance": [0.01, 0.05, 0.1, 0.15, 0.2],
        "degree_influence": [0.01, 0.02, 0.03, 0.04, 0.05]
    }

    results = batch_run(
        VirusOnNetwork,
        parameters=parameters,
        iterations=50,
        max_steps=50,
        number_processes=None,
        data_collection_period=-1,
        display_progress=True
    )

    results_df = pd.DataFrame(results)
    results_df.to_csv("batch_run_results.csv")


if __name__ == '__main__':
    main()
