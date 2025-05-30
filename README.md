# 🏗️ YOLOv8 Object Detection App – Blueprint Door & Window Detector

Welcome to my deployed computer vision project using **YOLOv8 + Gradio**, designed to detect **doors and windows** in architectural **construction blueprints**.

<<<<<<< HEAD
![demo](https://github.com/ultralytics/assets/raw/main/yolov8/banner-yolov8.png)

=======
>>>>>>> c2caa1648319b36d0c6ab6c97aea64a4ac51aaaf
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

<<<<<<< HEAD
✅ Try it online: *(add your Hugging Face space URL here)*  
✅ Or run it locally:

```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/yolov8-gradio-demo
cd yolov8-gradio-demo
=======

```bash
git clone https://github.com/Sagarkeshave/WinDoorDetection_YOLO.git
>>>>>>> c2caa1648319b36d0c6ab6c97aea64a4ac51aaaf
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
<<<<<<< HEAD
- **Trained On**: Custom blueprint dataset with annotated door and window classes
=======
- **Trained On**: Custom blueprint dataset with annotated door and window classes.
>>>>>>> c2caa1648319b36d0c6ab6c97aea64a4ac51aaaf
- **Performance**: Optimized for fast inference on 2D plan layouts

---

<<<<<<< HEAD
## 🎯 Recruiter Notes

This project demonstrates:
- Custom model training and fine-tuning
=======
## 🎯 Notes

This project demonstrates:
- Custom model training.
>>>>>>> c2caa1648319b36d0c6ab6c97aea64a4ac51aaaf
- Practical use of object detection in architecture
- Real-world deployment using Hugging Face Spaces
- Building user-friendly ML apps with Gradio

---

## 🙋‍♂️ Author

<<<<<<< HEAD
**Your Name**  
[GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)

---

> ⭐ Feel free to connect with me to discuss AI in construction tech or computer vision applications!

=======
**SAGAR G. KESHAVE**  
[LinkedIn](https://www.linkedin.com/in/sagar-keshave-564916221/)

---
>>>>>>> c2caa1648319b36d0c6ab6c97aea64a4ac51aaaf
