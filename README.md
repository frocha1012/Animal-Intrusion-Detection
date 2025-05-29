
# 🐄 Animal Intrusion Detection (YOLOv5)

This project uses a YOLOv5 model to detect **wild and domestic animals** in images or live video.  
It is based on the [Animal-Intrusion-Detection repo](https://github.com/SaiSwarup27/Animal-Intrusion-Detection), and expands it with:

- ✅ A web app built with Flask (styled with Bootstrap)
- ✅ A Python desktop GUI (Tkinter)
- ✅ A camera-based detection script (original from repo)
- ✅ NEW: PDF report generation with bounding box preview

---

## 🧠 Overview of Tools

| Mode          | File                      | Description                                                                 |
|---------------|---------------------------|-----------------------------------------------------------------------------|
| 🧪 Web App     | `main.py` / `main_pdf_matching_web.py` | Upload 2 images, see detections, download PDF with boxes                    |
| 🖥 Desktop GUI | `app.py`                  | Simple windowed app with image upload and label display                     |
| 🎥 Camera Mode | `camera.py`               | Original webcam detection using YOLOv5                                      |

Model used: `yolov5/best.pt` (included in the repo)

---

## 🌐 Web App (Flask)

### 📦 Dependencies

```bash
pip install flask torch torchvision pillow opencv-python reportlab
```

### ▶️ How to Run

```bash
python main_pdf_matching_web.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

### 🖼 Features
- Upload 2 images
- Annotated YOLOv5 bounding boxes saved and shown
- Lists all detected animals with confidence
- ✅ PDF report generation:
  - One page per image
  - Labels and full image preview with boxes
  - Matching exactly what’s shown on the site

---

## 🖥 Desktop GUI (Tkinter)

### 📦 Dependencies

```bash
pip install torch torchvision pillow opencv-python
```

### ▶️ How to Run

```bash
python app.py
```

- Upload Image 1 and Image 2
- See side-by-side image previews
- Shows detections below each image

---

## 🎥 Camera Detection

### ▶️ How to Run

```bash
python camera.py
```

- Uses webcam to detect cattle/wildlife live
- Displays real-time bounding boxes
- Great for monitoring environments

---

## 🔧 Code Modifications from Original Repo

### ✅ 1. Web UI + Detection Results
- `main.py` and `main_pdf_matching_web.py` added
- `templates/index.html` uses Bootstrap
- `static/uploads/` stores raw and annotated images

---

### ✅ 2. PDF Report Generation

**New route added in Flask**:
```python
@app.route('/generate-pdf')
```

✅ Uses `reportlab`  
✅ Includes:
- Image detections
- Annotated full image (from YOLOv5)
- One page per image  
✅ Matches the exact detection shown on the webpage

---

### ✅ 3. OpenCV Error Fixed

To avoid crash from OpenCV drawing boxes:
Modified `yolov5/utils/plots.py`:
```python
self.im = im.copy()  # make array writeable
```

---

## 📁 Folder Structure

```
animal-intrusion-detection/
├── app.py                       ← Desktop GUI
├── main_pdf_matching_web.py     ← Final web app (with PDF sync)
├── camera.py                    ← Webcam detection
├── yolov5/
│   ├── best.pt
│   ├── utils/plots.py           ← MODIFIED
│   └── models/common.py         ← Used during result saving
├── static/uploads/              ← Web image output
├── templates/index.html         ← Web UI form
```

---

## 🙏 Credits

- **YOLOv5 by Ultralytics** – https://github.com/ultralytics/yolov5  
- **Original Dataset Repo** – https://github.com/SaiSwarup27/Animal-Intrusion-Detection  
- **Fork & Enhancements** – [frocha1012](https://github.com/frocha1012)

---

## ✅ Status

All 3 modes fully working:

- ✅ Web with PDF generation
- ✅ Desktop with label preview
- ✅ Camera with live boxes

Ready to test, share, or deploy.
