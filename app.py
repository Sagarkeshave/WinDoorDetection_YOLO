import gradio as gr
from ultralytics import YOLO
from PIL import Image
import numpy as np

model = YOLO("model/my_model.pt")

def detect_objects(image: Image.Image):
    results = model(image)
    im_bgr = results[0].plot()
    im_rgb = Image.fromarray(im_bgr[..., ::-1])

    detections = []
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = float(box.conf[0])
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        w, h = x2 - x1, y2 - y1
        detections.append({
            "label": label,
            "confidence": round(conf, 2),
            "bbox": [round(x1, 2), round(y1, 2), round(w, 2), round(h, 2)]
        })

    return im_rgb, {"detections": detections}

gr.Interface(
    fn=detect_objects,
    inputs=gr.Image(type="pil"),
    outputs=[
        gr.Image(type="pil", label="Detected Image"),
        gr.JSON(label="Detection Results")
    ],
    title="YOLOv8 Object Detection",
    description="Upload an image to detect objects using a YOLOv8 model."
).launch()
