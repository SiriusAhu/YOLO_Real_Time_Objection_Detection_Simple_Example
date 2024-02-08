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

### 4.1 我不使用GPU

`UltraLytics`提供了一个名为`ultralytics`的奇妙模块，其中包含了几乎所有使用`yolo`所需的包。

因此，你可以通过以下命令安装`ultralytics`：

```bash
pip install ultralytics
```

### 4.2 我需要GPU（推荐的方式）

不幸的是，通过测试，我发现`ultralytics`有时无法正确下载`torch`、`torchaudio`和`torchvision`的GPU版本。

相反，你需要手动安装它们。

> 你可以从这个网站获取文件：[torch stable download](https://download.pytorch.org/whl/torch_stable.html)
> 注意：带有`cuXXX`的版本是用于GPU的。

### 4.3 我需要GPU（不推荐的方式）

一个不推荐的方式是通过以下命令安装它们（如果你使用的是`CUDA 18`。cuda版本可以通过`nvcc --version`检查）：

```bash
pip install torch torchaudio torchvision --index-url https://download.pytorch.org/whl/cu118
```

> 对于其他cuda版本，请将`cu118`替换为`cuXXX`

然而，这种方法有时会下载它们的`CPU`版本。

例如，今天（2024.2.9），我使用了这种方式，但发现`torchvision`是`CPU`版本。

如果你也遇到了这个问题，你可以从上面提到的网站（[torch stable download](https://download.pytorch.org/whl/torch_stable.html)）下载`whl`文件，并手动安装它。

### 4.4 检查安装

你可以使用以下命令检查安装：

```bash
pip freeze
```

> 你可以通过检查它们的名称中是否包含`cuXXX`来检查`torch`、`torchaudio`、`torchvision`和`ultralytics`是否是GPU版本。

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