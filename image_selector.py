import os
import random
import shutil

# Specify the base folder containing subfolders with images
#base_folder = r'C:\Uni3rd\thirdY\finalDB\imagesDB'
#base_folder = r"C:\Uni3rd\thirdY\finalDB\newDatabase"
base_folder = r".\database"
final_output_folder = r'.\selectedImages'

# Create the 'selectedImages' folder within the final output folder if it doesn't exist
if not os.path.exists(final_output_folder):
    os.makedirs(final_output_folder)

def is_image_file(filename):
    return filename.lower().endswith(('.jpg', '.png', '.jpeg'))

# Iterate through each subfolder and its subdirectories
for root, dirs, files in os.walk(base_folder):
    # Exclude the 'selectedImages' folder by skipping the iteration
    if final_output_folder in root:
        continue
    
    image_files = [f for f in files if is_image_file(f)]
    
    # Check if there are images and if so, randomly select up to 6 images
    if image_files:
        selected_images = random.sample(image_files, min(6, len(image_files)))
        
        # Copy the selected images to the final output folder
        for img_path in selected_images:
            src_path = os.path.join(root, img_path)
            dest_path = os.path.join(final_output_folder, os.path.basename(root) + '_' + img_path)
            shutil.copy(src_path, dest_path)
            print(f"Copying '{img_path}' from folder '{root}' to '{final_output_folder}'")

print(f"Selected images have been copied to '{final_output_folder}'.")