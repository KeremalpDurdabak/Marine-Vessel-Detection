# Marine Vessel Detection with YOLOv7

This repository provides a marine vessel detection system using the state-of-the-art YOLOv7 model, trained on the COCO image dataset. It is designed to automate the process of data preparation, model training, and evaluation for marine vessel detection systems.
## Usage

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>

2. **Run the setup and training script**:
    ```chmod +x run.sh
    ./run.sh

## Summary
The script automatically downloads boat images and annotations from the COCO dataset and saves them in a dataset directory. It then splits the images into training and validation sets with an 80/20 ratio, organizing them into train and val directories. After training the YOLOv7 model with these images, the script tests the model using the validation set and displays the performance metrics.