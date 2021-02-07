# Configurations
import progressbar as pb

# build data
train_origin_path = '/data/shenzhonghai/dmo-captcha/train-origin'
trainPath = '/data/shenzhonghai/dmo-captcha/dmo-captcha-part1'
train_size = 8598

test_origin_path = '/data/shenzhonghai/dmo-captcha/test-origin'
testPath = '/data/shenzhonghai/dmo-captcha/dmo-captcha-part0'
test_size = 4122

modelName = 'effnet_lr4045_s32_m10_co_rot_trs_crop_FULL_borWhite_rsz128'
modelSavePath = '/data/shenzhonghai/dmo-captcha/models/'+modelName
modelPath = '/data/shenzhonghai/dmo-captcha/models/'+modelName+'.tar'

H = 112
W = 112

# train
Total = 140
batch_size = 256
learning_rate = 0.001
milestones = [4000, 4500]
weight_decay = 0.00000
dp = 0.00

widgets = ['Data Loading: ', pb.Percentage(),
           ' ', pb.Bar(marker='>', left='[', right=']', fill='='),
           ' ', pb.Timer(),
           ' ', pb.ETA(),
           ' ', pb.FileTransferSpeed()]
