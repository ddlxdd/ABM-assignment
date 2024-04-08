# ABM-assignment

# Virus on Network


I chose to replicate the “Virus on Network” model, which I think is a foundational example within agent-base modeling field. This model simulates the spread of virus through the random selected population. The core purpose of this model is to explore the dynamics of infectious disease like the pandemic we just experienced two years ago within a networked community, demonstrating how individual behaviors and network structures. The model allows for a more complex interactions and the emergent patterns of virus transmission, recovery, and resistance.

# Design concepts

I think the model followed the principles of epidemiology and network theory, aiming to produce and reflect the nature of spreading disease and maybe potentially exploring intervention methods to mitigate the outbreak. The model basically focuses on three states: susceptibility, infection, and resistance to capture the essence of an epidemic's progression. For the interaction, each agent in the model represents an individual who can be in one of the three states: susceptible, infected, or resistant. Agents interact based on the underlying network structure, with the probability of infection being contingent on these interactions. The original model emphasizes the stochastic nature of disease spread and the role of individual variance in susceptibility and recovery.

# Enhancements

I made two changes to the model:

# 1.	Superspreaders

I added a new agent to the model, which is superspreaders. In some of the spreading diseases, the superspreaders play a pivotal role in the dynamic epidemics. The superspreaders in my new model are individuals with a higher probability of transmitting the virus. These agents can disproportionately affect the spreading process of the virus across the network.

# 2.	Infection Probability Based on Network Degree

I also changed the original parameter and updated it to a new infection probability which is based on the network degree. This is for the individuals who have more or a degree of social interactions, I think those people may under a different transmission rate.

# Details

The enhanced model initializes with a network of agents connected randomly; A subset of these agents is infected at the outset to simulate the introduction of a virus into the population. After the modification, the model now also identifies a small percentage of agents as superspreaders and adjusts infection probabilities based on the network degree of each agent. The model operates with minimal external input data, relying instead on parameterized simulations to explore different scenarios. Parameters include the number of agents, average node degree, initial outbreak size, virus spread chance, recovery chance, and the newly added superspreader chance.

Superspreaders: I add a boolean attribute 'is_superspreader' to the 'VirusAgent' class, determined at initialization. The chance of an agent being a superspreader was set to 1% (or 0.01 probability), reflecting the rare but significant presence of superspreaders in the populations. When a superspreader attempted to infect neighbors, the virus spread chance was effectively doubled. This modification was handled in the 'try_to_infect_neighbors' method of the 'VirusAgent' class, where the infection probability was conditionally increased for superspreaders.

Infection Probability: I introduced a new user-controlled parameter, 'degree_influence', enabling dynamic adjustment of the degree-based infection probability modification through a slider. With this new 'degree_influence' parameter, we can manipulate the extent to which an agent's network degree affects its likelihood of infection. 


# Conclusion

My version introduces the superspreaders, which highlights the non-linear and often unpredictable nature of epidemic spread. Even a small number of highly connected individuals can significantly alter the course of an outbreak, underscoring the importance of targeted interventions. With the new parameter, I think the model offers a more detailed view of how individual-level factors and overall network architecture coalesce to shape the trajectory of disease spread.
