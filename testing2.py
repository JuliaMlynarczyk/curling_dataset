from ultralytics import YOLO
import os

# Load trained model
if not os.path.exists("runs/detect/train5/weights/best.pt"):
    print("Nie znaleziono best.pt — upewnij się, że model został wytrenowany.")
    exit(1)

model = YOLO("runs/detect/train5/weights/best.pt")

# Run on validation images and save results
results = model.predict("dataset/images/val", save=True, conf=0.3)

