import cv2

img = cv2.imread('data/lena.jpg', 0)    # load image as array

print(img)

cv2.imshow('image', img)                # show image window with 'image' title
k = cv2.waitKey(0)                      # keep window showing the image

if k == 27:
    cv2.destroyAllWindows()             # press esc button to destroy window
elif k == ord('s'):
    cv2.imwrite('lena_copy.jpg', img)   # press 's' button to save and copy image
    cv2.destroyAllWindows()