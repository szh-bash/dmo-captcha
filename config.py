# Configurations
import progressbar as pb

# build data
train_origin_path = '/data/shenzhonghai/dmo-captcha/part1-clean'
trainPath = '/data/shenzhonghai/dmo-captcha/part1-64x42'
train_size = 8598

test_origin_path = '/data/shenzhonghai/dmo-captcha/part0-clean'
testPath = '/data/shenzhonghai/dmo-captcha/part0-64x42'
test_size = 8598

modelName = 'effnet_lr4045_s32_m30_co_rot_trs_crop_FULL_borWhite_sz64'
modelSavePath = '/data/shenzhonghai/dmo-captcha/models/'+modelName
modelPath = '/data/shenzhonghai/dmo-captcha/models/'+modelName+'.tar'

H = 64
W = 64

# train
Total = 160
batch_size = 256
learning_rate = 0.001
milestones = [3700, 4000]
weight_decay = 0.0005
dp = 0.00

widgets = ['Data Loading: ', pb.Percentage(),
           ' ', pb.Bar(marker='>', left='[', right=']', fill='='),
           ' ', pb.Timer(),
           ' ', pb.ETA(),
           ' ', pb.FileTransferSpeed()]
