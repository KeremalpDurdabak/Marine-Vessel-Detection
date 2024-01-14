#!/bin/bash

# Exit on any error
set -e

# Setup Environment and Dependencies
conda create -n yolov7 python=3.9 -y
conda activate yolov7
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install requests pycocotools

# Clone YOLOv7 and Prepare Dataset
git clone https://github.com/WongKinYiu/yolov7.git
python ../get_dataset.py
mv ../dataset/train yolov7/data/
mv ../dataset/val yolov7/data/

# Train and Test YOLOv7 Model
cd yolov7
python train.py --img 640 --batch 16 --epochs 50 --data data/boat_dataset.yaml --weights yolov7.pt
python val.py --weights runs/train/exp/weights/best.pt --data data/boat_dataset.yaml --img 640 --conf 0.5 --batch 16 --task test

# Display Performance Metrics
results_file='runs/test/exp/results.txt'
if [ -f "$results_file" ]; then
    cat $results_file
else
    echo "Results file not found."
fi

# Clean up
conda deactivate
