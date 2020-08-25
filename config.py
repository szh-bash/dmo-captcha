# Configurations
import progressbar as pb

# build data
train_origin_path = '/data/shenzhonghai/dmo-captcha/train-origin'
trainPath = '/data/shenzhonghai/dmo-captcha/dmo-captcha-part1'
train_size = 8598

test_origin_path = '/data/shenzhonghai/dmo-captcha/test-origin'
testPath = '/data/shenzhonghai/dmo-captcha/dmo-captcha-part0'
test_size = 4122

H = 112
W = 112

# train
Total = 100
batch_size = 128
learning_rate = 0.001
weight_decay = 0.00000
modelSavePath = '/data/shenzhonghai/dmo-captcha/models/resnet_36_56_m30_co_clean6'
# test
modelPath = '/data/shenzhonghai/dmo-captcha/models/resnet_36_56_m30_co_clean6.tar'
dp = 0.00

widgets = ['Data Loading: ', pb.Percentage(),
           ' ', pb.Bar(marker='>', left='[', right=']', fill='='),
           ' ', pb.Timer(),
           ' ', pb.ETA(),
           ' ', pb.FileTransferSpeed()]
