import torch
import cv2

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/best.pt')

# Initialize webcam
cap = cv2.VideoCapture(1)  # 0 is the default webcam #1 C922 PRO

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference
    results = model(frame)

    # Render results
    results.render()

    # Display the frame
    cv2.imshow('Animal Intrusion Detection', results.ims[0])

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
