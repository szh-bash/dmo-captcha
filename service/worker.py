import os
import time
from recognizer import predict

path = 'D:/Game/DigimonMasters/Code_AI/question/'
# path = /pic
if __name__ == '__main__':
    while True:
        dir = os.listdir(path)
        for ids in dir:
            if (ids[-4]=='.'):
                print(path+ids)
                answer = predict(path+ids)
                os.rename(path+ids, path+str(answer))
                print(answer)
        time.sleep(4)
