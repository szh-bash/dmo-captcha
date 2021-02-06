import cv2
import numpy as np
# import torch
import torchvision.transforms as trans
from config import H, W


_OH = 64
_OW = 64
_CH = 12
_CW = 12
MinS = 112
MaxS = 116


class Augment:
    rng = np.random

    def cutout(self, img):
        img = img.copy()
        if self.rng.rand() < 0.5:
            y = int(self.rng.rand() * _OH)
            x = int(self.rng.rand() * _OW)
            img[y:y+_CH, x:x+_CW, :] = 0
        return img

    def rotate(self, img):
        img = img.copy()
        if self.rng.rand() < 0.3:
            ang = self.rng.rand()*30-15
            mat = cv2.getRotationMatrix2D((_OH / 2, _OW / 2), ang, 1)
            img = cv2.warpAffine(img, mat, (_OH, _OW), borderValue=[255, 255, 255])
        return img

    def trans(self, img):
        img = img.copy()
        if self.rng.rand() < 0.3:
            dh = (self.rng.rand()*_OH - _OH/2)*0.3
            dw = (self.rng.rand()*_OW - _OW/2)*0.1
            mat = np.float32([[1, 0, dh], [0, 1, dw]])
            img = cv2.warpAffine(img, mat, (_OH, _OW), borderValue=[255, 255, 255])
        return img

    def resize(self, img):
        img = img.copy()
        new_size = self.rng.randint(MinS, MaxS+1)
        # new_size = 256
        new_size = (new_size, new_size)
        img = cv2.resize(img, new_size)
        return img

    def crop(self, img):
        img = img.copy()
        dh = img.shape[0] - H
        dw = img.shape[1] - W
        y = int(self.rng.rand()*dh)
        x = int(self.rng.rand()*dw)
        return img[y:y+H, x:x+W, :]

    def flip(self, img):
        img = img.copy()
        if self.rng.rand() < 0.5:
            img = img[:, ::-1, :]
        return img

    def run(self, img, label):
        img = cv2.copyMakeBorder(img, 0, 0, 11, 11, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        # img = self.cutout(img)
        img = self.rotate(img)
        img = self.trans(img)
        img = self.resize(img)
        img = self.crop(img)
        img = np.transpose(img, [2, 0, 1])
        img = (img - 127.5) / 128.0
        return img, label
