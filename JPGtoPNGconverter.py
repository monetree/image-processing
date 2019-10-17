import sys
import os
from PIL import Image

# input formt from command line
# python JPGtoPNGconverter.py pokedex/ new/
    # here pokedex is out current images
    # and converted image will store in new folder
    # it will convert all image to png format bu looping through it.

# grab first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not create one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through pokedex
# convert images to png
# save to the new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done')
