import tflearn
import numpy as np

from utils import load_train_data
from model_builder import vgg16_2

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# VGG 16
MODEL_NAME = "VGG16_basic_128x128"
NUM_CLASS = 2

# Load Dataset
train_data = load_train_data(
    name="train_data_{}x{}.npy",
    resize_pics=(128, 128))

# Dataset reshaping
X, Y = train_data[:, 0], train_data[:, 1]
X = np.array([i for i in X])
Y = np.array([i for i in Y])
logging.debug("{}, {}".format(X.shape, Y.shape))

# Training
model = tflearn.DNN(
    vgg16_2(NUM_CLASS),
    checkpoint_path='checkpoint/model_{}'.format(MODEL_NAME),
    max_checkpoints=1,
    tensorboard_verbose=0,
    tensorboard_dir="log")
logging.debug("Model building finish")

model.fit(
    X, Y,
    n_epoch=10,
    validation_set=0.1,
    shuffle=True,
    show_metric=True,
    batch_size=64, 
    snapshot_epoch=False,
    snapshot_step=500,
    run_id=MODEL_NAME)

model.save("model/" + MODEL_NAME)
