import matplotlib.pyplot as plt
from model import VirusOnNetwork

# Initialize the model
model = VirusOnNetwork(
    num_nodes=100,
    avg_node_degree=4,
    initial_outbreak_size=10,
    virus_spread_chance=0.4,
    recovery_chance=0.3,
    superspreader_chance=0.1, 
    degree_influence=0.05 
)


steps = 50
for i in range(steps):
    model.step()

# Collect data
results = model.datacollector.get_model_vars_dataframe()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(results['Susceptible'], label='Susceptible')
plt.plot(results['Infected'], label='Infected')
plt.plot(results['Resistant'], label='Resistant')
plt.xlabel('Time Steps')
plt.ylabel('Number of Agents')
plt.title('Disease Spread Dynamics')
plt.legend()
plt.grid(True)
plt.show()