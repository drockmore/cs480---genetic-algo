import random
import config
import numpy as np
from PIL import Image, ImageDraw
import config


def generate_individual():
    """Generate a random individual of triangles."""
    return [generate_random_triangle() for _ in range(config.NUM_TRIANGLES)]

def generate_random_triangle():
    """Generate a random triangle with points and greyscale color."""
    
    width, height = config.IMAGE_SIZE
    
    grayscale_value = random.randint(0, 255)
    return {
        'points': [(random.randint(0, width), random.randint(0, height)) for _ in range(3)],
        'color': (grayscale_value, grayscale_value, grayscale_value, 50),
    }


def render_individual(individual):
    """Render the entire individual of triangles onto a single greyscale image."""
    
    width, height = config.IMAGE_SIZE
    image = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(image, 'RGBA')

    # Draw each triangle onto the canvas
    for triangle in individual:
        draw.polygon(triangle['points'], fill=triangle['color'])
    image = image.convert("RGB")
    return np.array(image)


def mutate(triangle):
    """Apply mutation to a single triangle with selective and minor adjustments."""
    
    width, height = config.IMAGE_SIZE
    
    modification_amount = 1 #random.randint(1, 4)

    mutate = random.random() < config.MUTATION_RATE
    
    #if mutate == False and random.random() < .01:
    #   return generate_random_triangle()

    if mutate == True:
        if random.choice([True, False]):
            # Mutate one point in the triangle
            point_index = random.randint(0, 2)  # Choose one of the three points
            x, y = triangle['points'][point_index]
            # Add or subtract 2 from x or y, ensuring the new point is within bounds
            x += random.choice([-modification_amount, modification_amount])
            y += random.choice([-modification_amount, modification_amount])
            x = max(0, min(width, x))
            y = max(0, min(height, y))
            triangle['points'][point_index] = (x, y)
        else:
            # Mutate the color slightly
            color_adjustment = random.choice([-modification_amount, modification_amount])
            modified_color = max(0, min(255, triangle['color'][0] + color_adjustment))
            triangle['color'] = (modified_color, modified_color, modified_color, 50)
    return triangle
