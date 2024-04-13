import os
from rembg import remove

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for image in os.listdir(input_folder):
        input_image_path = os.path.join(input_folder, image)
        output_image_path = os.path.join(output_folder, f'{os.path.splitext(image)[0]}_nobg.png')

        try:
            with open(input_image_path, 'rb') as i, open(output_image_path, 'wb') as o:
                input_data = i.read()
                output_data = remove(input_data)
                o.write(output_data)
                print(f'Processed {image}.')
        except Exception as e:
            print(f'ERROR: Could not process {image}. Error: {e}')

if __name__ == '__main__':
    input_folder_path = f'C:\\Uni3rd\\thirdY\\finalDB\\selectedImages'
    output_folder_path = f'C:\\Uni3rd\\thirdY\\finalDB\\afterEdit'
    process_images(input_folder_path, output_folder_path)
