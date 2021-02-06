import os
import time
from recognizer import predict

# path = 'D:/Game/DigimonMasters/Code_AI/IShiled/question/'
path = '/data/shenzhonghai/dmo-captcha/pic/'
# path = 'C:/pic/'
if __name__ == '__main__':
    while True:
        dir = os.listdir(path)
        for ids in dir:
            if not('_' in ids) and ids[-4:] == '.jpg':
                timer = time.time()
                print(path+ids)
                try:
                    answer = predict(path+ids)
                except:
                    print('Error: recognization failed!')
                else:
                    timer = time.time() - timer
                    os.rename(path+ids, path+ids[:-4]+'_'+str(answer)+'.jpg')
                    print('Time: %.2fs' % timer)
                    print('Result: %s' % answer)
        time.sleep(1)
