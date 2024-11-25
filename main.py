# main.py
import config
from genetic_algorithm.fitness_modified import fitness_function
from genetic_algorithm.individual import generate_individual, render_individual, mutate
from genetic_algorithm.selection_controller import selection_controller
from genetic_algorithm.crossover_controller import crossover_controller
import cv2
from genetic_algorithm.progress_windows import show_generation
from genetic_algorithm.image_helpers import load_target_image, save_individual_image


def initialize_population():
    """Initialize a population with random individuals."""
    population = []
    for _ in range(config.POPULATION_SIZE):
        triangle_array = generate_individual()
        population.append(triangle_array)
    return population
           

def get_convergence_rate(fitnesses, first_fitness_score):
    """Calculate the % to conversion."""
    return ( 1 - (min(fitnesses) / first_fitness_score) ) * 100

def genetic_algorithm():
    
    # Initialize a single array of triangles
    population = initialize_population()
    best_individual_index = 0
    
    # Load target image as array
    target_image_array = load_target_image()
    first_fitness_score = -1

    for generation in range(config.NUM_GENERATIONS):
        
        # Calculate fitness for each individual in the population
        fitnesses = []
        for individual in population:
            individual_image_arr = render_individual(individual)
            fitnesses.append(fitness_function(target_image_array, individual_image_arr))
        
        if first_fitness_score == -1:
            first_fitness_score = min(fitnesses)
        
        #Get convergence rate
        convergence_percent = get_convergence_rate(fitnesses, first_fitness_score)
        
        # Create a new population from the top 5 individuals using the fitnes
        sorted_fitness = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i])
        new_population = [] #[population[sorted_fitness[i]] for i in range(5)]
        
        #new_population = [population[best_individual_index], population[[1])]]

    
            
        # Selection and Crossover
        selected_individuals, non_selected_individuals = selection_controller(population, fitnesses)

        # Create offspring
        offspring = crossover_controller(selected_individuals)
        
        # Add offspring to the new population
        new_population.extend(offspring)
        
        # Mutation: Apply mutation to the rest of the population
        for individual in non_selected_individuals:
            mutated_individual = [mutate(triangle) for triangle in individual]
            new_population.append(mutated_individual)
  
        # Display the best individual in the current generation
        best_individual_index = fitnesses.index(min(fitnesses))
        show_generation(render_individual(population[best_individual_index]), generation, min(fitnesses), convergence_percent)

        # Replace the population with the new one, limiting size to POPULATION_SIZE
        population = new_population[:config.POPULATION_SIZE]

        # Save the best individual image every IMAGE_PROGRESS_ITERATIONS generations
        if(generation % config.IMAGE_PROGRESS_ITERATIONS == 0):
            save_individual_image(render_individual(population[best_individual_index]), generation)
  
        # Break if convergence is 100% or reached the maximum number of generations
        if(convergence_percent >= 100 or generation == config.NUM_GENERATIONS - 1):
            save_individual_image(render_individual(population[best_individual_index]), 'final')
            break
            
        # Log the best fitness in the current generation
        print(f"Generation {generation} ({len(offspring)}) - Convergence: {convergence_percent}%,  Best Fitness: {min(fitnesses)}: {max(fitnesses)}")
        
        # Small delay for display
        cv2.waitKey(1)
    
    cv2.destroyAllWindows()
    return



if __name__ == "__main__":
    # Load target image to get dimensions
    best_individual = genetic_algorithm()
    
    save_individual_image(best_individual[0], config.NUM_GENERATIONS)
    # Render and save the best-matching image

