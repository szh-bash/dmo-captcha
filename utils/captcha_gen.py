from captcha.image import ImageCaptcha
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


number = [str(i) for i in range(10)]
ALPHABET = [chr(i+ord('A')) for i in range(26)]
captcha_content = number+ALPHABET+['#', '@', '%']


def gen_captcha(captcha_set, captcha_len=4):

    # captcha_content 构成验证码的字符list
    # captcha_len 验证码的长度
    res_str = np.random.choice(captcha_set, captcha_len)
    res = ImageCaptcha().generate(res_str)
    res = Image.open(res)
    res = np.array(res)
    return res, res_str


if __name__ == '__main__':
    captcha, captcha_str = gen_captcha(captcha_content, captcha_len=6)
    print(captcha_str)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.set_title(captcha_str)
    ax.imshow(captcha)
    plt.show()
