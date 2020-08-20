# Configurations
import progressbar as pb

# build data
captcha_origin_path = '/data/shenzhonghai/dmo-captcha/train-origin'
captchaPath = '/dev/shm/dmo-captcha-part0'
test_origin_path = '/data/shenzhonghai/dmo-captcha/test-origin'
testPath = '/dev/shm/dmo-captcha-part1'

# train
Total = 100
batch_size = 64
learning_rate = 0.001
weight_decay = 0.00000
modelSavePath = '/data/shenzhonghai/dmo-captcha/models/vgg16_32_48'
# test
modelPath = '/data/shenzhonghai/dmo-captcha/models/vgg16_32_48_5000.pt'
dp = 0.00

widgets = ['Data Loading: ', pb.Percentage(),
           ' ', pb.Bar(marker='>', left='[', right=']', fill='='),
           ' ', pb.Timer(),
           ' ', pb.ETA(),
           ' ', pb.FileTransferSpeed()]
