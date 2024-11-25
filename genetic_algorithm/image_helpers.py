import config
import numpy as np
from PIL import Image  # Ensure Image and ImageDraw are imported

def load_target_image():
    """Load, convert to RGBA with grayscale values, and resize the target image."""
    
    # Convert the image to grayscale and save for reference
    target_image_initial = Image.open(config.TARGET_IMAGE_PATH).convert('L').resize(config.IMAGE_SIZE)
    target_image_initial.save("images/target/target_grayscale.png")
    
    # Load the grayscale image
    target_image = Image.open("images/target/target_grayscale.png").convert('RGBA').resize(config.IMAGE_SIZE)

    
    # Convert to a NumPy array to retain RGBA values
    return np.array(target_image)

def save_individual_image(individual_image_arr, generation):
    """Save the image array as a PNG file."""

    # Convert the image array to a PIL Image and save it as a PNG
    individual_image = Image.fromarray(np.uint8(individual_image_arr))  # Convert array to uint8 if needed
    individual_image.save(f"images/matches/gen_{generation}.png")