import os
import re
import cv2
import torch
import numpy as np
from model.vggnet.vgg16 import Vgg16
from loss import ArcMarginProduct as ArcFace
from config import test_origin_path, testPath, widgets, modelPath

filePath = ''
H = 64
W = 42
MinS = 224
MaxS = 256
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
print("Default Class:", classes)


def predict(net, arc, device):
    img = np.array(cv2.imread(filePath), dtype=float)
    for idx in range(6):
        img_single = img[:, index[idx]:index[idx] + W, :]
        size = (MaxS+MinS) // 2
        st = (size-224) // 2
        img_single = cv2.resize(img_single, (size, size))
        img_single = img_single[st:st+224, st:st+224, :]
        img_single = (np.transpose(img_single, [2, 0, 1])-127.5)/128
        img_single = torch.from_numpy(np.array([img_single])).float()
        label = torch.from_numpy(np.array([0])).long()
        feat = arc(net(img_single.to(device)), label.to(device), 'test')
        label = torch.argmax(feat, dim=1).cpu().numpy()
        img_single = img[:, index[idx]:index[idx] + W, :]
        label_chr = chr(trans[label[0]])
        dir_path = os.path.join("%s/%c" % (testPath, label_chr))
        # print(label[0]+1, dir_path)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        cv2.imwrite(os.path.join("%s/%d.jpg" % (dir_path, cnt[label[0]])), img_single)
        cnt[label[0]] += 1


if __name__ == '__main__':
    res = 0
    count = 0
    device = torch.device('cuda:0')
    model = Vgg16().cuda()
    print(model)
    model.load_state_dict({k.replace('module.', ''): v for k, v in torch.load(modelPath)['net'].items()})
    model.eval()  # DropOut/BN
    arc = ArcFace(4096, classes).cuda()
    arc.load_state_dict({k.replace('module.', ''): v for k, v in torch.load(modelPath)['arc'].items()})
    model.cpu()
    arc.cpu()
    print(model, arc)

    print('origin:', count)
    print('result:', res)
    print(np.sort(cnt[0:classes]))