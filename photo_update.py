import os

images_folder = 'frames6'
labels_folder = 'labels6'

image_files = {os.path.splitext(f)[0] for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))}
label_files = {os.path.splitext(f)[0] for f in os.listdir(labels_folder) if os.path.isfile(os.path.join(labels_folder, f))}

extra_images = image_files - label_files

for image_name in extra_images:
    for ext in ['.jpg', '.jpeg', '.png', '.bmp']:
        image_path = os.path.join(images_folder, image_name + ext)
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Usunięto: {image_path}")