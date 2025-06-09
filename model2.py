from ultralytics import YOLO

# Load model (YOLOv8s as example)
model = YOLO('yolov8m.pt')

# Train
try:
    model.train(
        data='dataset/data.yaml',
        epochs=5,
        imgsz=640,
        batch=4
    )
except Exception as e:
    print(f"Błąd podczas treningu: {e}")

# Validate
model.val(data='dataset/data.yaml')

# Inference
results = model('prediction/image.jpg', save=True)

# Print results
print(results)

# Print summary
print("Training and validation completed. Results saved in 'prediction/results'.")
