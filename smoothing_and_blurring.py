import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      # matplotlib read image as rgb color

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)                 # good for removing salt and pepper noise
bf = cv2.bilateralFilter(img, 9, 75, 75)        # noise removal while keeping the edge sharp

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'BilateralFilter']
images = [img, dst, blur, gblur, median, bf]

for i in range(len(titles)):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()