# 简介

> 声明：本文档为机翻，仅供参考。

本仓库是一个简易的[YOLO](https://pjreddie.com/darknet/yolo/)实施目标检测的例子。

其提供了一个基本的`Python`程序，用于从摄像头捕获视频并实时检测物体。

# 需求

为了运行本仓库，你需要按照以下步骤进行。

至于环境，我建议使用`python>=3.8`。（我使用的是`python=3.12`）

# 如何使用？

## 1. 克隆本仓库

```bash
git clone https://github.com/SiriusAhu/YOLO_Real_Time_Objection_Detection_Simple_Example
```

## 2. 创建虚拟环境

如果你使用`Anaconda`，你可以通过以下命令创建一个虚拟环境：

```bash
conda create -n <env_name> python=3.12
```

> 这里，`<env_name>`是你的虚拟环境的名称。
> 例如：`conda create -n yolo python=3.12`

## 3. 激活你的虚拟环境

```bash
conda activate <env_name>
```

## 4. 安装所需的包

### 4.1 我不使用GPU（直接安装`ultralytics`）

`UltraLytics`提供了一个名为`ultralytics`的奇妙模块，其中包含了几乎所有使用`yolo`所需的包。

因此，你可以通过以下命令安装`ultralytics`：

```bash
pip install ultralytics
```

### 4.2 我需要GPU（手动安装`torch`、`torchaudio`、`torchvision`，然后安装`ultralytics`）
不幸的是，通过测试，我发现`ultralytics`有时无法正确下载GPU版本的`torch`、`torchaudio`和`torchvision`。相反，你需要手动安装它们。

请按照[PyTorch官方网站](https://pytorch.org)中的`INSTALL PYTORCH`部分首先安装`torch`、`torchaudio`和`torchvision`。

命令类似于（但不要直接复制粘贴，你需要检查网站以获取正确的命令）：

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
### 4.3 检查安装

你可以使用以下命令检查安装：

```bash
pip freeze
```

> 你可以通过检查它们的名称中是否包含`cuXXX`来检查`torch`、`torchaudio`、`torchvision`和`ultralytics`是否是GPU版本。

然后，为了进一步检查你是否正确安装了`torch`，你可以在`Python`中运行以下代码：

```python
import torch
print(torch.cuda.is_available())
```
如果返回`True`，那么你已经正确安装了`torch`。

## 5. 运行程序

只需使用`python`（在你的虚拟环境中）执行`run.py`。

```bash
python run.py
```

> 注意：点击`Q`退出程序。

### 5.1 参数

目前，只提供了一些参数：

1. `-m`或`--model`：要使用的模型。输入`8n`以使用YOLOv8n，输入`5s`以使用YOLOv5s。（默认：`8n`）
2. `-v`或`--verbose`：设置为`True`以获取`model.predict()`的详细输出。（默认：`False`）
3. `-d`或`--device`：要使用的设备。`0`表示CPU，`1`表示GPU。（默认：`0`）
4. `-c`或`--camera`：要使用的摄像头。`0`表示第一个摄像头。索引是基于你的系统的摄像头索引。如果遇到错误，请尝试更改此值。（默认：`0`）