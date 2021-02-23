import matplotlib.pyplot as plt
import numpy as np
import cv2

def ROI(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    return cv2.bitwise_and(img, mask)

def drow_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=4)
            print(line)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

#image = cv2.imread('data/road.jpg')
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def process(image):
    #print(image.shape)
    height = image.shape[0]
    width = image.shape[1]

    ROI_vertices = [
        (0, height),
        (width/2, height/1.3),
        (width, height)
    ]

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray_image, 10, 75, 75)
    canny_image = cv2.Canny(blur, 100, 120)
    cropped_image = ROI(canny_image, np.array([ROI_vertices], np.int32))
    lines = cv2.HoughLinesP(cropped_image,
                            rho=2,
                            theta=np.pi/180,
                            threshold=50,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=100)
    image_with_lines = drow_the_lines(image, lines)
    return image_with_lines, cropped_image, canny_image

cap = cv2.VideoCapture('data/Lane-Detection.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    #frame = process(frame)
    cv2.imshow('frame', process(frame)[0])
    #cv2.imshow('cropped', process(frame)[1])
    #cv2.imshow('canny', process(frame)[2])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()