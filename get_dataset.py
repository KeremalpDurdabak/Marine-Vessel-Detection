import os
import requests
from pycocotools.coco import COCO
import shutil
import random
import zipfile

# Setup directories
annotations_path = 'dataset/annotations/'
images_path = 'dataset/images/'
train_images_path = 'dataset/train/images/'
val_images_path = 'dataset/val/images/'
for path in [annotations_path, images_path, train_images_path, val_images_path]:
    os.makedirs(path, exist_ok=True)

# Download and unzip COCO annotations
coco_url = 'http://images.cocodataset.org/annotations/annotations_trainval2017.zip'
annotations_zip_path = os.path.join(annotations_path, 'annotations_trainval2017.zip')
if not os.path.exists(annotations_zip_path):
    annotations_zip = requests.get(coco_url)
    with open(annotations_zip_path, 'wb') as file:
        file.write(annotations_zip.content)
    with zipfile.ZipFile(annotations_zip_path, 'r') as zip_ref:
        zip_ref.extractall(annotations_path)

# Initialize COCO API and download boat images
coco = COCO(os.path.join(annotations_path, 'annotations/instances_train2017.json'))
cat_ids = coco.getCatIds(catNms=['boat'])
img_ids = coco.getImgIds(catIds=cat_ids)
downloaded_images = []
for img_id in img_ids:
    img_info = coco.loadImgs(img_id)[0]
    img_url = img_info['coco_url']
    img_filename = os.path.join(images_path, img_info['file_name'])
    with open(img_filename, 'wb') as img_file:
        img_file.write(requests.get(img_url).content)
    downloaded_images.append(img_filename)

# Split and organize dataset
random.shuffle(downloaded_images)
split_index = int(len(downloaded_images) * 0.8)
for img in downloaded_images[:split_index]:
    shutil.move(img, os.path.join(train_images_path, os.path.basename(img)))
for img in downloaded_images[split_index:]:
    shutil.move(img, os.path.join(val_images_path, os.path.basename(img)))
