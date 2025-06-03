import os
import random
import shutil

img_dir = "images"
label_dir = "labels"
output_dir = "dataset"
split_ratio = 0.8

# Create output folders
for split in ["train", "val"]:
    os.makedirs(f"{output_dir}/images/{split}", exist_ok=True)
    os.makedirs(f"{output_dir}/labels/{split}", exist_ok=True)

# Get all image filenames
image_files = [f for f in os.listdir(img_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(image_files)

# Split
split_index = int(len(image_files) * split_ratio)
train_files = image_files[:split_index]
val_files = image_files[split_index:]

def move_files(file_list, split):
    for file_name in file_list:
        base_name = os.path.splitext(file_name)[0]
        shutil.copy(os.path.join(img_dir, file_name), f"{output_dir}/images/{split}/{file_name}")
        label_file = f"{base_name}.txt"
        if os.path.exists(os.path.join(label_dir, label_file)):
            shutil.copy(os.path.join(label_dir, label_file), f"{output_dir}/labels/{split}/{label_file}")

move_files(train_files, "train")
move_files(val_files, "val")