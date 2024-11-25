from genetic_algorithm.selection import rank_based_selection

def selection_controller(population, fitnesses):
    """Select individuals based on their rank."""
    selected_individuals, non_selected_individuals = rank_based_selection(
        population, 
        fitnesses,
        10,    
    )
    
    return selected_individuals, non_selected_individuals
