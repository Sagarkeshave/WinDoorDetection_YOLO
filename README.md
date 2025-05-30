# 🏗️ YOLOv8 Object Detection App – Blueprint Door & Window Detector

Welcome to my deployed computer vision project using **YOLOv8 + Gradio**, designed to detect **doors and windows** in architectural **construction blueprints**.

---

## 🔍 About the App

This application showcases a deep learning model trained on blueprint images to identify:
- 🚪 **Doors**
- 🪟 **Windows**

The goal was to automate detection in architectural layouts and assist with digitizing or verifying blueprint components.

---

## 💡 How it Works

- The app is powered by a **custom-trained YOLOv8** model.
- You can **upload a blueprint image** via the Gradio interface.
- The model will return:
  - ✅ An **annotated image** showing detections
  - ✅ A **JSON output** with detection details in this format:

```json
{
  "detections": [
    {"label": "door", "confidence": 0.91, "bbox": [x, y, w, h]},
    {"label": "window", "confidence": 0.84, "bbox": [x, y, w, h]}
  ]
}
```

---

## 🚀 How to Use

1. Upload a construction blueprint image.
2. View the image with annotated bounding boxes.
3. Review the detection results in JSON format.


```bash
git clone https://github.com/Sagarkeshave/WinDoorDetection_YOLO.git
pip install -r requirements.txt
python app.py
```

---

## 🧠 Tech Stack

| Tool        | Purpose                              |
|-------------|--------------------------------------|
| YOLOv8      | Object detection                     |
| Ultralytics | Model training & inference framework |
| Gradio      | Web interface for inference          |
| Hugging Face Spaces | App hosting platform         |

---

## 📦 Model Info

- **Framework**: [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- **Trained On**: Custom blueprint dataset with annotated door and window classes.
- **Performance**: Optimized for fast inference on 2D plan layouts

---

## 🎯 Notes

This project demonstrates:
- Custom model training.
- Practical use of object detection in architecture
- Real-world deployment using Hugging Face Spaces
- Building user-friendly ML apps with Gradio

---

## 🙋‍♂️ Author

**SAGAR G. KESHAVE**  
[LinkedIn](https://www.linkedin.com/in/sagar-keshave-564916221/)

---
