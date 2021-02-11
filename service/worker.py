import os
import time
from recognizer import predict
from cfg import path


def label():
    dir = os.listdir(path)
    for ids in dir:
        if ids[-4:] == '.jpg':
            os.rename(path + ids, path+ids[-10:])


def work():
    dir = os.listdir(path)
    for ids in dir:
        if not ('_' in ids) and ids[-4:] == '.jpg':
            timer = time.time()
            answer = predict(path + ids)
            timer = time.time() - timer
            ids = ids.upper()
            try:
                os.rename(path + ids, path+str(ids[:-4] == answer)+'_' + str(answer) + '.jpg')
            except:
                pass
            else:
                pass
            print('Time: %.2fs' % timer)
            print('Result: %s' % answer)
            print()


if __name__ == '__main__':
    # label()
    # exit(0)
    # work()
    # exit(0)
    count = 0
    while True:
        dir = os.listdir(path)
        for ids in dir:
            if not('_' in ids) and ids[-4:] == '.jpg':
                timer = time.time()
                count += 1
                print('Pid: %d (%s) @%s' % (count, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), path+ids))
                try:
                    answer = predict(path+ids)
                except:
                    print('Error: recognization failed!')
                    count -= 1
                else:
                    timer = time.time() - timer
                    os.rename(path+ids, path+ids[:-4]+'_'+str(answer)+'.jpg')
                    print('Time: %.2fs' % timer)
                    print('Result: %s' % answer)
                print()
        time.sleep(1)
