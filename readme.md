# Genetic Algorithm

## Overview
This project is a crossword solver that processes crossword variables and solves them based on predefined configurations.

## Requirements
- Python 3.8 or higher
- Virtual environment setup (optional but recommended)
- Windows os for opencv-python (Displays the progress)

## Installation
```
pip install -r requirements.txt
```

### Running the program
```
python main.py
```

### Configuration
The configuration for the program is located in config.py and has the follow variables:
```
NUM_GENERATIONS = 10000000 # Number of generations to run

POPULATION_SIZE = 25 # Number of individuals in each generation

NUM_TRIANGLES = 200 # Number of triangles per individual

MUTATION_RATE = .05 # Probability of mutation per triangle

IMAGE_SIZE = (16,16) # Target image size (width, height)

IMAGE_PROGRESS_ITERATIONS = 10000  # Number of iterations between each image output

TARGET_IMAGE_PATH = "images/target/target_simple.png" # Location of the target image
```

### Output
When the program is ran, a gray scale version of the target will be created and saved
under "/images/target/target_grayscale.png", this will overwrite the previous grayscale
image. Image progress outputs will be saved under "/images/matches/gen_{iteration}.png"

A popup window will also be displayed that shows the current image progress with the
generation count and current fitness. Further this information will also be available 
in the terminal. 