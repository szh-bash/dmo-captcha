import re
import sys
import cv2
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import Parameter
import numpy as np
sys.path.append("..")

modelPath = 'C:/DATA/vgg16_32_48.tar'

H = 64
W = 42
size = (224 + 256) // 2
st = (size - 224) // 2
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


class Vgg16(nn.Module):
    def __init__(self):
        super(Vgg16, self).__init__()

        # 3 * 224 * 224
        self.conv1_1 = nn.Conv2d(3, 64, 3, padding=(1, 1))  # 64 * 224 * 224
        self.conv1_2 = nn.Conv2d(64, 64, 3, padding=(1, 1))  # 64 * 224* 224
        self.maxpool1 = nn.MaxPool2d((2, 2))  # pooling 64 * 112 * 112

        self.conv2_1 = nn.Conv2d(64, 128, 3, padding=(1, 1))  # 128 * 112 * 112
        self.conv2_2 = nn.Conv2d(128, 128, 3, padding=(1, 1))  # 128 * 112 * 112
        self.maxpool2 = nn.MaxPool2d((2, 2))  # pooling 128 * 56 * 56

        self.conv3_1 = nn.Conv2d(128, 256, 3, padding=(1, 1))  # 256 * 56 * 56
        self.conv3_2 = nn.Conv2d(256, 256, 3, padding=(1, 1))  # 256 * 56 * 56
        self.conv3_3 = nn.Conv2d(256, 256, 3, padding=(1, 1))  # 256 * 56 * 56
        self.maxpool3 = nn.MaxPool2d((2, 2))  # pooling 256 * 28 * 28

        self.conv4_1 = nn.Conv2d(256, 512, 3, padding=(1, 1))  # 512 * 28 * 28
        self.conv4_2 = nn.Conv2d(512, 512, 3, padding=(1, 1))  # 512 * 28 * 28
        self.conv4_3 = nn.Conv2d(512, 512, 3, padding=(1, 1))  # 512 * 28 * 28
        self.maxpool4 = nn.MaxPool2d((2, 2))  # pooling 512 * 14 * 14

        self.conv5_1 = nn.Conv2d(512, 512, 3, padding=(1, 1))  # 512 * 14 * 14
        self.conv5_2 = nn.Conv2d(512, 512, 3, padding=(1, 1))  # 512 * 14 * 14
        self.conv5_3 = nn.Conv2d(512, 512, 3, padding=(1, 1))  # 512 * 14 * 14
        self.maxpool5 = nn.MaxPool2d((2, 2))  # pooling 512 * 7 * 7

        # view

        self.fc1 = nn.Linear(512 * 7 * 7, 4096)
        self.fc2 = nn.Linear(4096, 4096)

    def forward(self, x):
        # x.size(0)即为batch_size
        in_size = x.size(0)

        out = self.conv1_1(x)  # 224
        out = F.relu(out)
        out = self.conv1_2(out)  # 224
        out = F.relu(out)
        out = self.maxpool1(out)  # 112

        out = self.conv2_1(out)  # 112
        out = F.relu(out)
        out = self.conv2_2(out)  # 112
        out = F.relu(out)
        out = self.maxpool2(out)  # 56

        out = self.conv3_1(out)  # 56
        out = F.relu(out)
        out = self.conv3_2(out)  # 56
        out = F.relu(out)
        out = self.conv3_3(out)  # 56
        out = F.relu(out)
        out = self.maxpool3(out)  # 28

        out = self.conv4_1(out)  # 28
        out = F.relu(out)
        out = self.conv4_2(out)  # 28
        out = F.relu(out)
        out = self.conv4_3(out)  # 28
        out = F.relu(out)
        out = self.maxpool4(out)  # 14

        out = self.conv5_1(out)  # 14
        out = F.relu(out)
        out = self.conv5_2(out)  # 14
        out = F.relu(out)
        out = self.conv5_3(out)  # 14
        out = F.relu(out)
        out = self.maxpool5(out)  # 7

        # 展平
        out = out.view(in_size, -1)

        out = self.fc1(out)
        out = F.relu(out)
        out = self.fc2(out)
        out = F.relu(out)

        return out


class ArcMarginProduct(nn.Module):

    def __init__(self, in_features, out_features):
        super(ArcMarginProduct, self).__init__()
        self.weight = Parameter(torch.FloatTensor(out_features, in_features))
        nn.init.xavier_uniform_(self.weight)

    def forward(self, inputs):
        cosine = F.linear(F.normalize(inputs), F.normalize(self.weight))
        return cosine


def predict():
    # filePath = 'D:/DigimonMasters/Code_AI/test-origin/720857789003916874.jpg'
    res = ''
    print('Loading Time: %.5fs' % (time.time()-load))
    run = time.time()
    img = np.array(cv2.imread(input()), dtype=float)

    for idx in range(6):
        image = img[:, index[idx]:index[idx] + W, :]
        image = cv2.resize(image, (size, size))
        image = image[st:st+224, st:st+224, :]
        image = (np.transpose(image, [2, 0, 1])-127.5)/128
        image = torch.from_numpy(np.array([image])).float()
        feat = arc(net(image))
        lb = torch.argmax(feat, dim=1).numpy()[0]
        res += chr(trans[lb])

    print('Running Time: %.5fs' % (time.time()-run))
    return res


if __name__ == '__main__':
    load = time.time()
    net = Vgg16().cpu()
    net.load_state_dict({k.replace('module.', ''): v for k, v in torch.load(modelPath)['net'].items()})
    net.eval()
    arc = ArcMarginProduct(4096, classes).cpu()
    arc.load_state_dict({k.replace('module.', ''): v for k, v in torch.load(modelPath)['arc'].items()})
    arc.cpu()
    label = predict()
    print(label.upper())
