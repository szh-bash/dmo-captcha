import os
import cv2
import numpy as np
import progressbar as pb
from config import captcha_origin_path, captchaPath, widgets
import re

H = 64
W = 42
index = [14, 54, 94, 124, 164, 204]
num = [0]*132
cnt = [0]*132
count = 0
for i in range(132):
    if re.match(r'[\da-z%@#]', chr(i)):
        count += 1
        num[i] = count
print("Default Class:", count)


def build(filename):
    img_path = os.path.join("%s/%s" % (captcha_origin_path, filename))
    img = np.array(cv2.imread(img_path), dtype=float)
    for idx in range(6):
        label = filename[idx]
        if label.isupper():
            label = label.lower()
        img_single = img[:, index[idx]:index[idx] + W, :]
        dir_path = os.path.join("%s/%s" % (captchaPath, label))
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        cv2.imwrite(os.path.join("%s/%d.jpg" % (dir_path, cnt[num[ord(label)]])), img_single)
        cnt[num[ord(label)]] += 1


if __name__ == '__main__':
    res = 0
    count = 0
    if not os.path.exists(captchaPath):
        os.mkdir(captchaPath)
    print(captchaPath)
    path_dir = os.listdir(captcha_origin_path)
    pgb = pb.ProgressBar(widgets=widgets, maxval=687).start()
    for allDir in path_dir:
        build(allDir)
        res += 6
        count += 1
        pgb.update(count)
    pgb.finish()
    print('origin:', count)
    print('result:', res)
    print(np.sort(cnt[1:39]))
