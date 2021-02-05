import os
import time
from recognizer import predict

path = 'D:/Game/DigimonMasters/Code_AI/IShiled/question/'
# path = /pic
if __name__ == '__main__':
    while True:
        dir = os.listdir(path)
        for ids in dir:
            if not('_' in ids):
                timer = time.time()
                print(path+ids)
                answer = predict(path+ids)
                timer = time.time() - timer
                os.rename(path+ids, path+ids[:-4]+'_'+str(answer)+'.jpg')
                print('Time: %.2fs' % timer)
                print('Result: %s' % answer)
        time.sleep(0.5)
