import glob
import random
import os
from PIL import Image

# Create a new directory for the output images
output_dir = 'C:/Uni3rd/thirdY/database/combinedImages'
os.makedirs(output_dir, exist_ok=True)

# Number of output images to generate
num_outputs = 10  # Change this to the number of output images you want

# Number of images to select for each output
num_images = 2  # Change this to the number of images you want

# Get the list of images from the specified directory
images = glob.glob('C:/Uni3rd/thirdY/finalDB/selectedImages/*.png') + glob.glob('C:/Uni3rd/thirdY/finalDB/selectedImages/*.jpg')

for i in range(num_outputs):
    # Open the background image
    img_bg = Image.new('RGBA', (1000, 1000), (255, 255, 255, 255))  # Create a larger white canvas
    width, height = img_bg.size

    # Randomly select a subset of images
    selected_images = random.sample(images, num_images)

    for img_path in selected_images:
        img = Image.open(img_path)

        # Rotate the image by a random angle
        angle = random.randint(0, 360)
        img = img.rotate(angle, expand=True)

        # Generate a random position on the canvas
        x = random.randint(0, width - img.width)
        y = random.randint(0, height - img.height)

        # Paste the image onto the background
        img_bg.paste(img, (x, y), mask=img)

    # Save the result in the new directory
    img_bg.save(os.path.join(output_dir, f'result{i+1}.png'), 'PNG')

print(f"Generated {num_outputs} composite images in '{output_dir}'.")
