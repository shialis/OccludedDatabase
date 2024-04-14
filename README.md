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
   - Run `image_selector.py` to select images from the specified directory.
   - Specify the directory path and the number of images to select.

2. **Background Removal**:
   - After selecting the images, run `background_remover.py` to remove backgrounds from the selected objects.
   - This process will create a folder for each image containing the background-removed objects.

3. **Image Composition**:
   - Once backgrounds are removed, run `image_combinator.py` to compose the final images, with a blank canvas background.
   - Alternatively, run `image_combinator_background.py` to compose the final images, with the background being an image of your choice. Note, you will need to adjust the file name in the file, currently the default name is `background.png`. Also, you will need to update the `runner.py` file to use this file instead of `image_combinator.py`.

4. **Running All Processes at Once**:
   - Use the provided runner file,  to execute all functionalities at once.

## Installing Required Packages

Install the `numpy` package by running the following command:
```bash
pip install numpy
```

Install the `rembg` package by running the following command:
```bash
pip install rembg
```
If you plan to use rembg with GPU support, you need to check if your system supports onnxruntime-gpu. If it does, you can install rembg with GPU support using the command 
```bash
pip install rembg[gpu]
```

Install the `Pillow` package (Python Imaging Library) by running the following command:
```bash
pip install pillow
```

## Output

After running the processes, a custom dataset will be generated containing images with occluded objects. Each image will have multiple objects combined onto a single canvas or background.

Sample Images
Here are some sample images generated by the dataset generator:

([https://github.com/shialis/OccludedDatabase/assets/126681215/b8d64e60-ed40-475b-839b-ef619d4b3618])


([https://github.com/shialis/OccludedDatabase/assets/126681215/ae5a28b8-8df9-4f30-aa9d-a7ae82fbace3])

([https://github.com/shialis/OccludedDatabase/assets/126681215/c32f4c5f-ab0e-4052-b4b5-7c8e899c00f5])
