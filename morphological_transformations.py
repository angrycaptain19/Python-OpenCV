import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5, 5), np.uint8)
print(kernel)

dilation = cv2.dilate(mask, kernel, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)    # erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)   # dilation followed by erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)     # the different between the dilation and the erotion of an image
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)       # the different between the image and the opening of an image

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(len(titles)):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()