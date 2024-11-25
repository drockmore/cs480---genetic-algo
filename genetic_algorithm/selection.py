# genetic_algorithm/selection.py
# This function was created with the help of chat gpt 4.o

import random

def rank_based_selection(population, fitnesses, num_selected):
    """Select individuals based on their rank."""
    
    # Rank individuals by fitness (lower fitness is better, so we sort ascending)
    ranked_indices = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i])
    
    # Assign ranks and calculate selection probabilities based on rank
    N = len(population)
    rank_probabilities = [(2 * (N - rank) / (N * (N + 1))) for rank in range(N)]
    
    # Normalize probabilities to ensure they sum to 1
    rank_probabilities_sum = sum(rank_probabilities)
    normalized_probabilities = [p / rank_probabilities_sum for p in rank_probabilities]
    
    # Select individuals based on normalized rank probabilities
    selected_indices = random.choices(ranked_indices, weights=normalized_probabilities, k=num_selected)
    selected = [population[i] for i in selected_indices]
    
    # Identify non-selected individuals
    non_selected_indices = set(ranked_indices) - set(selected_indices)
    non_selected = [population[i] for i in non_selected_indices]
    
    return selected, non_selected

