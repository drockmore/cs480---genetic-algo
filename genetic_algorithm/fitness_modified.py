import config 

def fitness_function(target_image_array, individual_image_array):
    """Calculate fitness by comparing only pixels inside each triangle in the context of the full population image."""
    
    width, height = config.IMAGE_SIZE
        # Ensure images are the same size
    # Get dimensions of the images

    fitness_score = 0
    for i in range(height):
        for j in range(width):
            
            # Get the absolute value of the difference in pixel values excluding the alpha channel
            fitness_score += abs(int(target_image_array[i][j][0]) - int(individual_image_array[i][j][0]))
            fitness_score += abs(int(target_image_array[i][j][1]) - int(individual_image_array[i][j][0]))
            fitness_score += abs(int(target_image_array[i][j][2]) - int(individual_image_array[i][j][0]))

            # Add the absolute difference to the fitness score
            # Return the fitness score
            
    return fitness_score


def fitness_function_target(target_image_array):
    """Calculate fitness of just the target."""
    
    width, height = config.IMAGE_SIZE
        # Ensure images are the same size
    # Get dimensions of the images

    fitness_score = 0
    for i in range(height):
        for j in range(width):
            
            # Get the absolute value of the difference in pixel values excluding the alpha channel
            fitness_score += int(target_image_array[i][j][0])
            fitness_score += int(target_image_array[i][j][1])
            fitness_score += int(target_image_array[i][j][2])

            # Add the absolute difference to the fitness score
            # Return the fitness score
            
    return fitness_score