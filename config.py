# Configurations
import progressbar as pb

# build data
captcha_origin_path = '/data/shenzhonghai/code'
captchaPath = '/dev/shm/dmo-captcha'

# train
Total = 300
batch_size = 64
learning_rate = 0.001
weight_decay = 0.00000
modelSavePath = '/data/shenzhonghai/dmo-captcha/models/demo_5k'
# test
modelPath = '/data/shenzhonghai/dmo-captcha/models/demo.tar'
testPath = '/dev/shm/dmo-captcha'
# featPath = '/data/shenzhonghai/lfw/mtLfw-base-feat-fc2-35000/'
dp = 0.00

widgets = ['Data Loading: ', pb.Percentage(),
           ' ', pb.Bar(marker='>', left='[', right=']', fill='='),
           ' ', pb.Timer(),
           ' ', pb.ETA(),
           ' ', pb.FileTransferSpeed()]
