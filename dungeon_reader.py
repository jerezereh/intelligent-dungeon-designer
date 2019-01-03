# Scans a dungeon map, dividing it into small segments, and converts them into an array of numbers

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# use a nn to accurately identify elements such as a corner, hallway, or wall segment, enumerating them and storing them as an array