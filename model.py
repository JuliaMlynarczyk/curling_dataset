from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640
)

model.val()
results = model("prediction/image.jpg", save=True)