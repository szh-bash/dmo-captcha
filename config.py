# Configurations
import progressbar as pb

# build data
train_origin_path = '/data/shenzhonghai/dmo-captcha/train-origin'
trainPath = '/data/shenzhonghai/dmo-captcha/dmo-captcha-part1'
train_size = 8598

test_origin_path = '/data/shenzhonghai/dmo-captcha/test-origin'
testPath = '/data/shenzhonghai/dmo-captcha/dmo-captcha-part0'
test_size = 4122

modelName = 'effnet_s32_m10_nco_rot_trs_crop_FULL_borWhite'
modelSavePath = '/data/shenzhonghai/dmo-captcha/models/'+modelName
modelPath = '/data/shenzhonghai/dmo-captcha/models/'+modelName+'.tar'

H = 112
W = 112

# train
Total = 130
batch_size = 256
learning_rate = 0.001
milestones = [3000, 3600]
weight_decay = 0.00000
dp = 0.00

widgets = ['Data Loading: ', pb.Percentage(),
           ' ', pb.Bar(marker='>', left='[', right=']', fill='='),
           ' ', pb.Timer(),
           ' ', pb.ETA(),
           ' ', pb.FileTransferSpeed()]
