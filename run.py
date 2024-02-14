from ultralytics import YOLO
import cv2
import numpy as np
import torch
import os
import argparse

WINDOW_NAME = "YOLO REAL TIME OBJECT DETECTION!!!"

args = argparse.ArgumentParser()
args.add_argument("-m", "--model", type=str, default="8n", help="Model to use: Enter \"8n\" for YOLOv8n, \"5s\" for YOLOv5s")
args.add_argument("-v", "--verbose", action="store_true", default=False, help="\"True\" or \"False\" | Set to True for verbose output for \"model.predict()\"")
args.add_argument("-d", "--device", type=int, default=1, help="\"0\" or 1 | Device to use: 0 for CPU, 1 for GPU | If you have more than one GPU, you must be able to modify this code by yourself ^^")
args.add_argument("-c", "--camera", type=int, default=0, help="Camera to use: 0 for the first camera | Index is based on your system's camera index | Try to change this value if you meet errors")
args.add_argument("-mf", "--model_folder", type=str, default="models", help="Folder to save the model (under current directory) | Default: \"models\" (created if not exist)")

args = vars(args.parse_args())

_model_name = args["model"]
model_name = f"yolov{_model_name}.pt"
verbose = args["verbose"]
device = args["device"]
camera = args["camera"]
model_folder = os.path.join(os.getcwd(), args["model_folder"])

if not os.path.exists(model_folder):
    os.makedirs(model_folder)
    print(f"- Model folder not found. Created folder at {model_folder}.")

if device == 0:
    print("- Using CPU.")
    device = 'cpu'
else:
    is_cuda_available = torch.cuda.is_available()
    if is_cuda_available:
        print("- Using GPU.")
        device = 'cuda'
    else:
        print("- Sorry, `torch.cuda.is_available()` returned `False`.")
        device = 'cpu'
        print("- Using CPU.")

# Load the model: If not found, it will be downloaded to *current directory*
model = YOLO(os.path.join(model_folder, model_name))

# Open the camera
cap = cv2.VideoCapture(camera)

def show_result_info(result):
    boxes = result.boxes.xywh.cpu()
    origin_shape = result.boxes.orig_shape
    clss = result.boxes.cls.int().cpu().tolist()
    names = result.names
    confs = result.boxes.conf.float().cpu().tolist()

    print(f"- Origin Shape: {origin_shape}")
    for box, cls, conf in zip(boxes, clss, confs):
        x, y, w, h = box
        label = f"{names[cls]}: {conf:.2f}"
        x1, y1, x2, y2 = int(x - w / 2), int(y - h / 2), int(x + w / 2), int(y + h / 2)
        print(f"- {label} at ({x1}, {y1}) to ({x2}, {y2})")

while cap.isOpened():
    # Read the frame
    ret, frame = cap.read()

    # Predict the frame
    results = model.predict(frame, verbose=verbose, device=device)
    img = np.squeeze(results[0].plot()) # Convert to numpy array

    # Verbose with the result
    if verbose:
        show_result_info(results[0])

    # Show the frame in opencv window
    cv2.imshow(WINDOW_NAME, img)

    # Press Q or close the window to exit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()