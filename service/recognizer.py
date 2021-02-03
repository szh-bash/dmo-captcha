import re
import cv2
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import Parameter
import numpy as np

from model.resnet.resnet import resnet50
modelPath = 'C:/DATA/dmo/resnet_36_56_m30_co_clean6.tar'


H = 64
W = 42
MinS = 112
MaxS = 128
size = (MinS+MaxS) // 2
st = (size - MinS) // 2
index = [14, 54, 94, 124, 164, 204]
num = [0]*132
cnt = [0]*132
trans = [0]*40
classes = 0
for i in range(132):
    if re.match(r'[\da-ce-pr-z%@#]', chr(i)):
        num[i] = classes
        trans[classes] = i
        classes += 1


class ArcMarginProduct(nn.Module):

    def __init__(self, in_features, out_features):
        super(ArcMarginProduct, self).__init__()
        self.weight = Parameter(torch.FloatTensor(out_features, in_features))
        nn.init.xavier_uniform_(self.weight)

    def forward(self, inputs):
        cosine = F.linear(F.normalize(inputs), F.normalize(self.weight))
        return cosine


def predict(filepath):
    res = ''
    img = np.array(cv2.imread(filepath), dtype=float)

    for idx in range(6):
        image = img[:, index[idx]:index[idx] + W, :]
        image = cv2.resize(image, (size, size))
        image = image[st:st+MinS, st:st+MinS, :]
        image = (np.transpose(image, [2, 0, 1])-127.5)/128
        image = torch.from_numpy(np.array([image])).float()
        feat = arc(net(image))
        lb = torch.argmax(feat, dim=1).numpy()[0]
        res += chr(trans[lb])

    return res.upper()


timer = time.time()
net = resnet50().cpu()
net.load_state_dict({k.replace('module.', ''): v for k, v in torch.load(modelPath, map_location='cpu')['net'].items()})
net.eval()
arc = ArcMarginProduct(2048*7*7, classes).cpu()
arc.load_state_dict({k.replace('module.', ''): v for k, v in torch.load(modelPath, map_location='cpu')['arc'].items()})
print('Load time:', time.time()-timer)
# net.cuda()
# arc.cuda()

if __name__ == '__main__':
    path = 'D:/Game/DigimonMasters/DATS v5.91/code.jpg'
    # path = 'D:/DigimonMasters/Code_AI/test-origin/720857789003916874.jpg'
    # path = '/data/shenzhonghai/dmo-captcha/test-origin/720857789003916874.jpg'
    timer = time.time()
    print(predict(path))
    print('Recognize time:', time.time()-timer)
