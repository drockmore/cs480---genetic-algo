from genetic_algorithm.crossover import multi_parent_uniform_crossover

def crossover_controller(selected_individuals):
    
    selection_size = len(selected_individuals)

    offspring = multi_parent_uniform_crossover(selected_individuals, selection_size)

    return offspring