import glob
import random
import os
from PIL import Image
from PIL import ImageChops

# Create a new directory for the output images
output_root = './outputs'
os.makedirs(output_root, exist_ok=True)

# Number of output images to generate
num_outputs = 10  # Change this to the number of output images you want

# List of different combinations (2, 3, 4, and 5 images)
combinations = [2, 3, 4, 5]

# Get the list of images from the specified directory
images = glob.glob('./afterEdit/*.png') + glob.glob('./afterEdit/*.jpg')

def scale_image(img, scale_factor):
    # Ensure that both width and height are under 300x300
    max_dimension = 300
    original_width, original_height = img.size
    
    # Resize the image if it exceeds 300x300
    if original_width > max_dimension or original_height > max_dimension:
        # Calculate the scaling factor to fit within 300x300
        resize_factor = min(max_dimension / original_width, max_dimension / original_height)
        new_size = (int(original_width * resize_factor), int(original_height * resize_factor))
        img = img.resize(new_size, Image.Resampling.LANCZOS)
    
    # Calculate the new size based on the provided scale factor
    new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
    
    # Resize the image
    img = img.resize(new_size, Image.Resampling.LANCZOS)
    
    return img

def calculate_coverage(img_bg, img):
    # Calculate the total number of pixels in the image
    total_pixels = img_bg.size[0] * img_bg.size[1]

    # Split the image into four sections
    width, height = img_bg.size
    section_width = width // 2
    section_height = height // 2

    # Calculate the coverage for each section
    topleft_coverage = _calculate_section_coverage(img, 0, 0, section_width, section_height)
    topright_coverage = _calculate_section_coverage(img, section_width, 0, section_width, section_height)
    bottomleft_coverage = _calculate_section_coverage(img, 0, section_height, section_width, section_height)
    bottomright_coverage = _calculate_section_coverage(img, section_width, section_height, section_width, section_height)

    # Calculate the overall coverage
    non_transparent_pixels = sum(p > 0 for p in img.getdata(3))
    overall_coverage = (non_transparent_pixels / total_pixels) * 100

    return {
        'topleft': topleft_coverage,
        'topright': topright_coverage,
        'bottomleft': bottomleft_coverage,
        'bottomright': bottomright_coverage,
        'overall': overall_coverage
    }

def _calculate_section_coverage(img, x, y, width, height):
    # Calculate the number of non-transparent pixels in the section
    non_transparent_pixels = 0
    for i in range(x, x + width):
        for j in range(y, y + height):
            pixel = img.getpixel((i, j))
            if pixel[3] > 0:
                non_transparent_pixels += 1

    # Calculate the total number of pixels in the section
    total_pixels = width * height

    # Calculate the coverage percentage for the section
    coverage = (non_transparent_pixels / total_pixels) * 100
    return coverage

def calculate_remaining_area(img_bg):
    # Convert the image to grayscale
    img_gray = img_bg.convert('L') 

    # Calculate the number of white pixels (i.e., pixels that are part of the remaining canvas)
    white_pixels = sum(p == 255 for p in img_gray.getdata())

    # Calculate the total number of pixels in the image
    total_pixels = img_bg.size[0] * img_bg.size[1]

    # Calculate the remaining area percentage
    remaining_area = (white_pixels / total_pixels) * 100

    return remaining_area

# Initialize the previous image position
prev_x, prev_y = 0, 0

for num_images in combinations:
    output_dir = os.path.join(output_root, f'comb{num_images}outputs')
    os.makedirs(output_dir, exist_ok=True)
    print(f"Creating output directory: {output_dir}")

    for i in range(num_outputs):
        # Open the background image
        img_bg = Image.new('RGBA', (1000, 800), (255, 255, 255, 255))  # Create a larger white canvas
        img_total = Image.new('RGBA', (1000, 800), (0, 0, 0, 0))  # Create a transparent canvas for total coverage
        width, height = img_bg.size

        # Randomly select a subset of images
        selected_images = random.sample(images, num_images)

        for img_path in selected_images:
            img = Image.open(img_path)

            # Scale the image by a random factor between 1 and 2
            scale_factor = random.uniform(1, 2)
            img = scale_image(img, scale_factor)

            # If the image is too large, resize it
            if img.width > 0.9 * width or img.height > 0.9 * height:
                img = img.resize((int(0.9 * width), int(0.9 * height)), Image.LANCZOS)

            # Rotate the image by a random angle
            angle = random.randint(0, 90)
            img = img.rotate(angle, expand=True)

            # Generate a random position on the canvas
            max_x = width - img.width
            max_y = height - img.height
            if max_x < 0 or max_y < 0:
                # Skip this image if it's larger than the canvas
                continue

            # Ensure the new position is at least 10% different in width and height from the previous image
            attempts = 0
            while True:
                x = random.randint(0, max_x)
                y = random.randint(0, max_y)
                if abs(x - prev_x) >= 0.3 * img.width and abs(y - prev_y) >= 0.3 * img.height:
                    break
                attempts += 1
                if attempts > 100000:  # Add a limit to the number of attempts
                    #print("Warning: Could not find a suitable position for the image after 100000 attempts.")
                    break

            # Update the previous image position
            prev_x, prev_y = x, y

            # Paste the image onto the background and the total coverage canvas
            img_bg.paste(img, (x, y), mask=img)
            img_total.paste(img, (x, y), mask=img)

        # Calculate and print the total coverage with three significant figures
        coverage_results = calculate_coverage(img_bg, img_total)
        overall_coverage = coverage_results['overall']
        overall_coverage_str = "{:.3g}".format(overall_coverage)
        print(f"Total coverage after creating image 'result{i+1}.png': {overall_coverage_str}%")

        # Print the coverage for each section
        print("Section coverages:")
        for section, coverage in coverage_results.items():
            if section != 'overall':
                section_coverage_str = "{:.3g}".format(coverage)
                print(f"{section.capitalize()} coverage: {section_coverage_str}%")

        # Add a space after each image
        print()

        # Save the result in the new directory
        output_path = os.path.join(output_dir, f'result{i+1}.png')
        img_bg.save(output_path, 'PNG')

    print(f"Finished with output directory: {output_dir}")
    print("-------------------------------------------------------------------------------------")    

print(f"Generated {num_outputs} composite images in separate directories under '{output_root}'.")
