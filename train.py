import random
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential,load_model
from keras.layers import Dense,Dropout,Activation,Flatten,Convolution2D,MaxPooling2D
from keras.optimizers import SGD
from keras.utils import np_utils
from keras import backend

from 加载数据集 import load_dataset,revise_image,IMAGE_SIZE

class Dataset:
    def __init__(self,path_name):
        #训练集
        self.train_images=None
        self.train_labels=None

        #验证集
        self.valid_images=None
        self.valid_labels=None

        #测试集
        self.test_images=None
        self.test_labels=None

        #数据集加载路径
        self.path_name=path_name

        #当前库采用的维度顺序
        self.input_shape=None

    #加载数据集并按照交叉验证的原则划分数据集并进行相关预处理工作
    def load(self,img_rows=IMAGE_SIZE,img_cols=IMAGE_SIZE,img_channels=3,nb_classes=2):
        #加载数据集
        images,labels=load_dataset(self.path_name)

