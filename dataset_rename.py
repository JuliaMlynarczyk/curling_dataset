import os
import shutil
from glob import glob

image_folders = ["frames0", "frames1", "frames2_7", "frames345", "frames6"]
label_folders = ["labels0", "labels1", "labels2_7", "labels345", "labels6"]

# Output folders
output_img = "images"
output_lbl = "labels"
os.makedirs(output_img, exist_ok=True)
os.makedirs(output_lbl, exist_ok=True)

# Processing
img_count = 0
for img_folder, lbl_folder in zip(image_folders, label_folders):
    print(f"Processing folder: {img_folder} and {lbl_folder}")
    for img_path in glob(os.path.join(img_folder, "*")):
        base = os.path.splitext(os.path.basename(img_path))[0]
        ext = os.path.splitext(img_path)[1]
        new_name = f"img_{img_count:05d}{ext}"
        new_label_name = f"img_{img_count:05d}.txt"

        shutil.copy(img_path, os.path.join(output_img, new_name))

        label_path = os.path.join(lbl_folder, f"{base}.txt")
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(output_lbl, new_label_name))

        img_count += 1

print(f"Copied and renamed {img_count} images and labels.")