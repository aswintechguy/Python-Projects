# install module
# pip install opencv-python

import cv2

# read the image
img = cv2.imread('test.jpg')
img = cv2.resize(img, (300, 300))

# display the image
cv2.imshow('original image', img)
cv2.waitKey(0)

# convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur the image for better detection
blur_img = cv2.GaussianBlur(img_gray, (3,3), 0)

# display the blur image
cv2.imshow('blur image', blur_img)
cv2.waitKey(0)

# canny edge detection
canny = cv2.Canny(blur_img, 100, 200)

# display the canny image
cv2.imshow('canny image', canny)
cv2.waitKey(0)

# laplacian edge detection
laplacian = cv2.Laplacian(blur_img, cv2.CV_64F)

# display the laplacian image
cv2.imshow('laplacian image', laplacian) 
cv2.waitKey(0)


cv2.destroyAllWindows()
