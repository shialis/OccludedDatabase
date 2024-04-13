# Custom Occluded Object Dataset Generator

This project aims to create a custom dataset for occluded object detection by mixing multiple objects from images and combining them into a single image or background. The process involves selecting objects from various images, removing their backgrounds, and then merging them onto a white canvas or background.

## Dataset Creation Process

The dataset creation process consists of three main functionalities, each implemented in a separate Python file:

1. **Image Selection**: Selects a customizable number of images from all subdirectories of a specified directory.
2. **Background Removal**: Removes the backgrounds from the selected objects in the images.
3. **Image Composition**: Combines the background-removed objects onto a single white canvas or background.

Additionally, there is a runner file provided that can be executed to run all these functionalities in sequence.

## Usage

1. **Image Selection**:
   - Run `seImages/selecting.py` to select images from the specified directory.
   - Specify the directory path and the number of images to select.

2. **Background Removal**:
   - After selecting the images, run `removesBG/main.py` to remove backgrounds from the selected objects.
   - This process will create a folder for each image containing the background-removed objects.

3. **Image Composition**:
   - Once backgrounds are removed, run `combineImages/combImagesFinal.py` to compose the final images, with a blank canvas background.
   - Alternatively, run `combineImages/combImagesFinalBackground.py` to compose the final images, with the background being an image of your choice.

4. **Running All Processes at Once**:
   - Use the provided runner file,  to execute all functionalities at once.

## Output
After running the processes, a custom dataset will be generated containing images with occluded objects. Each image will have multiple objects combined onto a single canvas or background.
