# Configurations
import progressbar as pb

# build data
captcha_origin_path = '/data/shenzhonghai/dmo-captcha/train-origin'
captchaPath = '/dev/shm/dmo-captcha-train'
test_origin_path = '/data/shenzhonghai/dmo-captcha/test-origin'
testPath = '/dev/shm/dmo-captcha-test'

# train
Total = 100
batch_size = 64
learning_rate = 0.001
weight_decay = 0.00000
modelSavePath = '/data/shenzhonghai/dmo-captcha/models/vgg16_224_256'
# test
modelPath = '/data/shenzhonghai/dmo-captcha/models/vgg16_224_256.tar'
testPath = '/dev/shm/dmo-captcha'
# featPath = '/data/shenzhonghai/lfw/mtLfw-base-feat-fc2-35000/'
dp = 0.00

widgets = ['Data Loading: ', pb.Percentage(),
           ' ', pb.Bar(marker='>', left='[', right=']', fill='='),
           ' ', pb.Timer(),
           ' ', pb.ETA(),
           ' ', pb.FileTransferSpeed()]
