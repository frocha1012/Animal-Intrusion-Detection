
from flask import Flask, render_template, request, send_file
from PIL import Image
import os
import torch
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load YOLOv5 model
model = torch.hub.load('yolov5', 'custom', path='yolov5/best.pt', source='local')
model.conf = 0.25

# Store detection results globally
detection_cache = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    global detection_cache
    detection_cache = {}

    if request.method == 'POST':
        for i in [1, 2]:
            file = request.files.get(f'image{i}')
            if file:
                raw_path = os.path.join(UPLOAD_FOLDER, f'image{i}.jpg')
                file.save(raw_path)

                results = model(raw_path)
                results.save(save_dir=UPLOAD_FOLDER)
                boxed_path = f'image{i}.jpg'

                df = results.pandas().xyxy[0]
                labels = [f"{row['name']} ({row['confidence']:.2f})" for _, row in df.iterrows()]
                detection_cache[f'image{i}'] = {
                    'path': boxed_path,
                    'labels': labels or ['Nenhum animal detectado.']
                }

    return render_template('index.html', detections=detection_cache)

@app.route('/generate-pdf')
def generate_pdf():
    global detection_cache
    pdf_path = 'static/report.pdf'
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    for i in [1, 2]:
        key = f'image{i}'
        if key in detection_cache:
            img_path = f'static/uploads/{key}.jpg'
            labels = detection_cache[key]['labels']

            # Header
            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, height - 50, f"Animal Detection - Image {i}")

            # Label list
            c.setFont("Helvetica", 11)
            y = height - 80
            for label in labels:
                c.drawString(70, y, f"- {label}")
                y -= 15

            y -= 10

            # Image preview
            try:
                c.drawImage(ImageReader(img_path), 50, 100, width=500, height=300)
            except Exception as e:
                c.drawString(70, y, f"[Image error: {e}]")

            c.showPage()

    c.save()
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
