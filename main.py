from flask import Flask, render_template, request
from PIL import Image
import os
import torch

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load YOLOv5 model
model = torch.hub.load('yolov5', 'custom', path='yolov5/best.pt', source='local')
model.conf = 0.25

@app.route('/', methods=['GET', 'POST'])
def index():
    detections = {}

    if request.method == 'POST':
        for i in [1, 2]:
            file = request.files.get(f'image{i}')
            if file:
                # Save raw uploaded image
                raw_path = os.path.join(UPLOAD_FOLDER, f'image{i}.jpg')
                file.save(raw_path)

                # Run YOLOv5 detection
                results = model(raw_path)

                # Save image with boxes (drawn by YOLOv5)
                results.save(save_dir=UPLOAD_FOLDER)
                boxed_path = f'image{i}.jpg'  # YOLO saves with same name

                # Get label data
                df = results.pandas().xyxy[0]
                labels = [f"{row['name']} ({row['confidence']:.2f})" for _, row in df.iterrows()]
                detections[f'image{i}'] = {
                    'path': boxed_path,
                    'labels': labels or ['Nenhum animal detectado.']
                }

    return render_template('index.html', detections=detections)

if __name__ == '__main__':
    app.run(debug=True)
