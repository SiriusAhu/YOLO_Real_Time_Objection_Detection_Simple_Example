# Introduction

This reporsitory is a simple example of [YOLO](https://pjreddie.com/darknet/yolo/) real-time object detection.

It provides a basic `Python` program to capture video from camera and detect objects in real-time.

# Requirements

To run this reporsitory, you need to follow the steps one by one.

As for the environment, I suggest using `python>=3.8`. (I use `python=3.12`)

# How to use?

## 1. Clone this repository

```bash
git clone https://github.com/SiriusAhu/YOLO_Real_Time_Objection_Detection_Simple_Example
```

## 2. Create a virtual environment

If you're using `Anaconda`, you can create a virtual environment by:

```bash
conda create -n <env_name> python=3.12
```

> Here, `<env_name>` is the name of your virtual environment.
> e.g. `conda create -n yolo python=3.12`

## 3. Activate your virtual environment

```bash
conda activate <env_name>
```

## 4. Install the required packages

> You can choose to install the packages in two ways: `CPU` or `GPU` version.

### 4.1 I won't use GPU: Directly install `ultralytics`

`UltraLytics` provides a fantastic module called `ultralytics`, which contains almost all the required packages for using `yolo`.

So you can just install `ultralytics` by:

```bash
pip install ultralytics
```

### 4.2 I need GPU: Manually install `torch`, `torchaudio`, `torchvision`, then install `ultralytics`

Unfortunately, by testing, I found that `ultralytics` sometimes doesn't download GPU version of `torch`, `torchaudio` and `torchvision` correctly.

Instead you need to install them manually.

Follow the `INSTALL PYTORCH` part in the [PyTorch official website](https://pytorch.org) to install `torch`, `torchaudio` and `torchvision` first.

The command is like this (but don't just copy and paste it, you need to check the website for the correct command):

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 4.3 Check the installation

You can use this command to check the installation:

```bash
pip freeze
```

> You can check if `torch`, `torchaudio`, `torchvision` and `ultralytics` are GPU versions by checking whether they contain `cuXXX` in their names.

Then for further check if you install `torch` correctly, you can run the following code in `Python`:

```python
import torch
print(torch.cuda.is_available())
```

If it returns `True`, then you have installed `torch` correctly.

## 5. Run the program

Just execute `run.py` with `python` (in your virtual environment)

```bash
python run.py
```

Note: Click `Q` to quit the program.

### 5.1 Arguments

Currently, only few arguments are provided:

1. `-m` or `--model`: Model to use. Enter `8n` for YOLOv8n, `5s` for YOLOv5s. (default: `8n`)
2. `-v` or `--verbose`: Set to `True` for verbose output for `model.predict()`. (default: `False`)
3. `-d` or `--device`: Device to use. `0` for CPU, `1` for GPU. (default: `0`)
4. `-c` or `--camera`: Camera to use. `0` for the first camera. Index is based on your system's camera index. Try to change this value if you meet errors. (default: `0`)