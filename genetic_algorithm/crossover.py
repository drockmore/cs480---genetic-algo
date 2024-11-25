import copy
import random

def multi_parent_uniform_crossover(parents, num_offspring):
    """Performs uniform crossover across multiple parents, generating the specified number of offspring."""
    offspring = []

    # Generate each offspring
    for _ in range(num_offspring):
        child = []
        
        # Perform crossover for triangle in the parents
        for i in range(len(parents[0])):  
            # Randomly select one parent for each point and color
            selected_color = random.choice(parents)[i]['color']
            selected_triangle = {
                'points': [
                    random.choice(parents)[i]['points'][j]
                    for j in range(3)
                ],
                'color': selected_color
            }
            child.append(copy.deepcopy(selected_triangle))
        
        offspring.append(child)
    
    return offspring
