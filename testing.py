import os
from ultralytics import YOLO

folder_path = "prediction"

files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
for i, filename in enumerate(files, 1):
    ext = os.path.splitext(filename)[1].lower()
    new_name = f"image{i:03d}{ext}"
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    os.rename(src, dst)
print(f"Renamed {len(files)} files.")

# 2. Labelowanie każdego zdjęcia po kolei i zapisywanie wyniku
model = YOLO("runs/detect/train/weights/best.pt")
files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
for filename in files:
    img_path = os.path.join(folder_path, filename)
    print(f"Processing {filename} ...")
    results = model(img_path, save=True)
print("Labeling done.")