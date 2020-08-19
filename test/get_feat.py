import sys
import torch
import numpy as np
import progressbar as pb

sys.path.append("..")
from init import DataReader
from model.vggnet.vgg16 import Vgg16
from torch.utils.data import DataLoader
from loss import ArcMarginProduct as ArcFace

from config import modelPath, widgets


# check = torch.load(modelPath)
# print(check)
# exit(0)
feats = []
test_Y = []


def save_feat(ft, lb, lim):
    ft = ft.cpu()
    lb = lb.cpu()
    for dx in range(lim):
        feats.append(ft[dx].data.numpy())
        test_Y.append(lb[dx].data.numpy())
        # ftx = ft[dx].data.numpy()
        # ftx = ftx.tolist()
        # pt = pd.DataFrame(data=ftx)
        # pt.to_csv(path+name+'/'+str(idx), mode='w', index=None, header=None)


# load data
batch_size = 1
data = DataReader('test')
data_loader = DataLoader(dataset=data, batch_size=batch_size, shuffle=False, pin_memory=True)

# load model
device = torch.device('cuda:0')
model = Vgg16().cuda()
print(model)
model.load_state_dict({k.replace('module.', ''): v for k, v in torch.load(modelPath)['net'].items()})
model.eval()  # DropOut/BN
arc = ArcFace(4096, data.type).cuda()
arc.load_state_dict({k.replace('module.', ''): v for k, v in torch.load(modelPath)['arc'].items()})
# print('epoch: %d, iter: %d, loss: %.5f, train_acc: %.5f' %
#       (checkpoint['epoch'], checkpoint['iter'], checkpoint['loss'], checkpoint['acc']))
# get feat
print('Calculating Feature Map...')
ids = 0
Total = (data.sample - 1) / batch_size + 1
pgb = pb.ProgressBar(widgets=widgets, maxval=Total).start()
for i, (inputs, labels) in enumerate(data_loader):
    feat = arc(model(inputs.to(device)), labels.to(device))
    save_feat(feat, labels, labels.size(0))
    pgb.update(i)
pgb.finish()
feats = np.array(feats)
test_Y = np.array(test_Y)
print(feats.shape)
print(np.argmax(feats, axis=1))
print(test_Y)
print('Test Accuracy:', np.sum(np.argmax(feats, axis=1) == test_Y)/Total)
