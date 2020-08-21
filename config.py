# Configurations
import progressbar as pb

# build data
captcha_origin_path = '/data/shenzhonghai/dmo-captcha/train-origin'
trainPath = '/dev/shm/dmo-captcha-part1'
train_size = 8598

test_origin_path = '/data/shenzhonghai/dmo-captcha/test-origin'
testPath = '/dev/shm/dmo-captcha-part0'
test_size = 4122

H = 112
W = 112

# train
Total = 100
batch_size = 128
learning_rate = 0.001
weight_decay = 0.00000
modelSavePath = '/data/shenzhonghai/dmo-captcha/models/resnet_1k'
# test
modelPath = '/data/shenzhonghai/dmo-captcha/models/resnet_1k.tar'
dp = 0.00

widgets = ['Data Loading: ', pb.Percentage(),
           ' ', pb.Bar(marker='>', left='[', right=']', fill='='),
           ' ', pb.Timer(),
           ' ', pb.ETA(),
           ' ', pb.FileTransferSpeed()]
