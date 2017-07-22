import cv2
import os
import numpy as np
from tqdm import tqdm

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

TRAIN_DIR = "../Cat_Dog/train"

def convert_to_one_hot_label(img_name):
    label = img_name.split(".")[0]
    return [1, 0] if label == "cat" else [0, 1]

def load_train_data(name="train_data_{}x{}.npy", resize_pics=(227, 227)):
    width = resize_pics[0]
    height = resize_pics[1]
    FILE_NAME = name.format(width, height)
    if os.path.exists(FILE_NAME):
        logging.info("load train data")
        train_data = np.load(FILE_NAME)
    else:
        logging.info("create train data")
        train_data = []
        for img_name in tqdm(os.listdir(TRAIN_DIR)):
            one_hot_label = convert_to_one_hot_label(img_name)
            path = os.path.join(TRAIN_DIR, img_name)
            img = cv2.imread(path)
            img = cv2.resize(img, (width, height))
            train_data.append([img, np.array(one_hot_label)])
        logging.info("finish load to memory")
        np.random.shuffle(train_data)
        logging.info("finish shuffle")
        np.save(FILE_NAME, train_data)
        logging.info("finish save to file")
    return train_data
