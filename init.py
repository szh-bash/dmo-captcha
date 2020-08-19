import cv2
import os
import torch
import numpy as np
from torch.utils.data import Dataset
import progressbar as pb
from utils.DataHandler import Augment, MaxS, MinS
from config import captchaPath, widgets
# lfw: 5749, 13233
# webface: 10575, 494414
# clean-webface: 10575, 455594
# dmo-captcha: 65, 4122


aug = Augment()


class DataReader(Dataset):
    type = 0
    sample = 0
    dataset = []
    label = []
    rng = np.random
    st = ''

    def __init__(self, st):
        self.st = st
        path_dir = os.listdir(captchaPath)
        print('Data Path:', captchaPath)
        pgb = pb.ProgressBar(widgets=widgets, maxval=4122).start()
        for allDir in path_dir:
            child = os.path.join('%s/%s' % (captchaPath, allDir))
            child_dir = os.listdir(child)
            for allSon in child_dir:
                son = os.path.join('%s/%s' % (child, allSon))
                if self.st == 'train':
                    self.dataset.append(cv2.imread(son))
                elif self.st == 'test':
                    self.dataset.append(cv2.imread(son))
                self.label.append(self.type)
                pgb.update(self.sample)
                self.sample += 1
            self.type += 1
        pgb.finish()
        print('Processing Method:', self.st)
        if self.st == 'train':
            self.dataset = np.array(self.dataset, dtype=float)
        elif self.st == 'test':
            self.dataset = np.array(self.dataset, dtype=float)
        self.label = np.array(self.label)
        print('Types:', self.type)
        print('Label:', self.label.shape)
        print('Label_value:', self.label[345:350])
        self.y = torch.from_numpy(self.label).long()
        print(self.y, self.y.type())

    def __getitem__(self, index):
        if self.st == 'train':
            image = self.dataset[index]
            image, label = aug.run(image, self.y[index])
            image = torch.from_numpy(image).float()
            return image, label
        elif self.st == 'test':
            # size = (MaxS+MinS) // 2
            size = 256
            idx = (size-224) // 2
            img = self.dataset[index]
            img = cv2.resize(img, (size, size))
            img = img[idx:idx+224, idx:idx+224, :]
            img = np.transpose(img, [2, 0, 1])
            img = torch.from_numpy((img-127.5)/128).float()
            return img, self.y[index]
        else:
            exit(-1)

    def __len__(self):
        return self.sample


if __name__ == '__main__':
    DataReader('train')
