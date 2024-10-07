# Dual-Domain Feature-Guided Task Alignment for Enhanced Small Object Detection

This repository contains the code for the paper **"Dual-Domain Feature-Guided Task Alignment for Enhanced Small Object Detection"**. The proposed method includes a Small Object Enhancement Pyramid (SOEP) and Task-Aligned Head (TAH) for improved detection of small objects, particularly in UAV images. The repository includes the implementation of the model, experiments, and evaluation metrics.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Experiments](#experiments)
- [Results](#results)

## Introduction

Small object detection is a challenge in images captured from UAVs, due to limited pixel resolution and frequent pooling in deep learning models. This project addresses these challenges with:
- **SOEP (Small Object Enhancement Pyramid)**: Enhances small object feature representation using frequency domain analysis.
- **TAH (Task-Aligned Head)**: Unifies classification and localization tasks to improve small object detection.

## Requirements

To run the code, you will need the following dependencies:

You can install the dependencies using requirements.txt:

pip install -r requirements.txt

### Installation
Clone the repository:

```bash
git clone https://github.com/RichardGuo0301/Dual-Domain-FTA.git
```
```bash
cd your-repo
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage
Training:

## Usage

### Training:

To train the model on the VisDrone dataset:

```bash
python train.py --dataset VisDrone --epochs 150
```
### Evaluation:

To evaluate the model on the test dataset:

```bash
python evaluate.py --dataset VisDrone --weights checkpoints/best_model.pth
```

## Model Architecture
The proposed architecture is built on the YOLOv8 framework, featuring:

- **SOEP**: Extracts high-frequency features using spectral analysis.
- **TAH**: Combines classification and localization tasks to improve alignment.
Refer to the diagram in the paper for a detailed view of the architecture.

## Experiments
Our experiments are conducted on the VisDrone dataset. The dataset consists of images from UAVs, and the models are trained and evaluated for small object detection. You can download the dataset from VisDrone Dataset.

### The default training settings:

- **Input image size**: 640x640
- **Batch size**: 4
- **Optimizer**: SGD with an initial learning rate of 0.01
- **Epochs**: 150

## Results
The model outperforms previous state-of-the-art models with an improvement of 12.7% in mAP@0.5 and 14.19% in mAP@0.5:0.95 on the VisDrone dataset.

| Model          | mAP@0.5 | mAP@0.5:0.95 |
|----------------|---------|--------------|
| Baseline YOLOv8| 34.6%   | 17.8%        |
| D2FTA (ours)   | 42.8%   | 25.9%        |
