import os
import glob
import random
import os
from PIL import Image
from rembg import remove


def main():
    # Get absolute paths
    base_path = './'
    
    # Execute each file in sequence
    execute_file(os.path.join(base_path, 'image_selector.py'))

    print("Starting Removing Backgrounds process")
    execute_file(os.path.join(base_path, 'background_remover.py'))
    execute_file(os.path.join(base_path, 'image_combinator.py'))

def execute_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    exec(code, globals())

if __name__ == "__main__":
    main()