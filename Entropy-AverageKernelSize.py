import PIL
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
from PIL import Image
import glob



def Filter(img, k):
    im = cv2.imread(img)
    kernel = np.ones((k, k), np.float32) / pow(k,2)
    dst = cv2.filter2D(im, -1, kernel)
    return dst

def Entropy(dst):
    im = Image.fromarray(dst)

    rgbhistogram = im.histogram()
    for rgb in range(3):
        totalPixels = sum(rgbhistogram[rgb * 256 : (rgb + 1) * 256])
        ent = 0.0
    for col in range(rgb * 256, (rgb + 1) * 256):
        freq = float(rgbhistogram[col]) / totalPixels
    if freq > 0:
        ent = ent + freq * math.log(freq, 2)
        ent = - ent
        return ent
    return -1

if  __name__ == "__main__":
    # INput image
    imname = 'Lewis.jpg'
    arrx = []
    arry = []

    for w in range(3, 15, 2):
        filtered = Filter(imname, w)
        ent = Entropy(filtered)
        if ent!= -1:
            arrx.append(w)
            arry.append(ent)

    print(arrx)
    print(arry)
    plt.plot(arry)
    plt.ylabel('Entropy')
    plt.show()