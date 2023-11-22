import torch

if torch.cuda.is_available():
    device = torch.device("cuda")
    print('There are %d GPU(s) available.' % torch.cuda.device_count())
    print('We will use the GPU:', torch.cuda.get_device_name(0))

else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")


import urllib
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
import torch
import torchvision
import torchvision.transforms as transforms
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torch.utils.data import DataLoader, Dataset
import os
from PIL import Image
import random
import xml.etree.ElementTree as ET
import time
import requests
from skimage.transform import resize

from bs4 import BeautifulSoup
import matplotlib.patches as patches
import albumentations as A


# path of images directory
dir_path  = '../gdrive/My Drive/detection_miniproject/archive/images'

# path of xml files directory
xml_path = "../gdrive/My Drive/detection_miniproject/archive/annotations"

#List of Image file name
file_list = os.listdir(dir_path)

# How many image files?
print('There are total {} images.'.format(len(file_list)))


def read_annot(file_name, xml_dir):  # file_name, xml_dir을 input으로 받아 bbox, labels를 return

    bbox = []  # 마스크의 바운딩 박스 좌표를 담음
    labels = []  # with_mask면 2, no_mask 1, mask_weared_incorrect 3

    annot_path = os.path.join(xml_dir, file_name[:-3] + 'xml')
    tree = ET.parse(annot_path)
    root = tree.getroot()

    # 각 마스크의 바운딩 박스 좌표
    for boxes in root.iter('object'):
        ymin = int(boxes.find("bndbox/ymin").text)
        xmin = int(boxes.find("bndbox/xmin").text)
        ymax = int(boxes.find("bndbox/ymax").text)
        xmax = int(boxes.find("bndbox/xmax").text)
        label = boxes.find('name').text

        bbox.append([xmin, ymin, xmax, ymax])

        if label == 'with_mask':
            label_idx = 2
        elif label == 'without_mask':
            label_idx = 1
        else:
            label_idx = 3
        labels.append(label_idx)

    return bbox, labels


def draw_boxes(img, boxes, labels, thickness=2):  # thickness : bounding box의 두께 2로 지정
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    text = []
    for box, label in zip(boxes, labels):
        box = [int(x) for x in box]
        if label == 2:  # with_mask 면 파란색 bounding box
            color = (255, 0, 0)
            text.append("with_mask")
        elif label == 1:  # with_mask가 아니면 빨간색 bounding box
            color = (0, 0, 225)  # red
            text.append("without_mask")
        else:  # weared_incorrect면 오렌지색 bounding box
            color = (0, 215, 255)  # orange
            text.append("mask_weared_incorrect")
        cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), color, thickness)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB), box[0], box[1], text

