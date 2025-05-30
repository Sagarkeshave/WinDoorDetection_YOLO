# 🏗️ YOLOv8 Object Detection App – Blueprint Door & Window Detector

Welcome to my deployed computer vision project using **YOLOv8 + Gradio**, designed to detect **doors and windows** in architectural **construction blueprints**.

![demo](https://github.com/ultralytics/assets/raw/main/yolov8/banner-yolov8.png)

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

✅ Try it online: *(add your Hugging Face space URL here)*  
✅ Or run it locally:

```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/yolov8-gradio-demo
cd yolov8-gradio-demo
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
- **Trained On**: Custom blueprint dataset with annotated door and window classes
- **Performance**: Optimized for fast inference on 2D plan layouts

---

## 🎯 Recruiter Notes

This project demonstrates:
- Custom model training and fine-tuning
- Practical use of object detection in architecture
- Real-world deployment using Hugging Face Spaces
- Building user-friendly ML apps with Gradio

---

## 🙋‍♂️ Author

**Your Name**  
[GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)

---

> ⭐ Feel free to connect with me to discuss AI in construction tech or computer vision applications!

