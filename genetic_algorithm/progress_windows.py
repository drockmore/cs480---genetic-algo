import cv2
import numpy as np

# This function was created with the help of chat gpt 4.o
def show_generation(image_array, generation_number, fitness_score, convergence_percent):
    """
    Displays an image in a pop-up window with generation number overlayed.
    """
    # Convert image array to BGR for OpenCV display
    bgr_image = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    
    resized_image = cv2.resize(bgr_image, (600, 600), interpolation=cv2.INTER_NEAREST)
    
    # Add text for generation count
    cv2.putText(
        resized_image, f'Generation: {generation_number}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    
    # Display fitness score information below the generation
    cv2.putText(
        resized_image, f'Fitness: {fitness_score} ({int(convergence_percent)}%)', (10, 50),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA
    )
    

    
    # Show the image in a pop-up window
    cv2.imshow('Generation Progress', resized_image)
    cv2.waitKey(1)  # Wait for a short time to allow OpenCV to update

