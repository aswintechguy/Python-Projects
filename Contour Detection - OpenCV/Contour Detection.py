# install module
# pip install opencv-python

import cv2

# load the image
image = cv2.imread('test1.jpg')
# resize the image
image = cv2.resize(image, (350, 350))
# display the image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# convert to grayscale
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# display the image
cv2.imshow('Gray Scale Image', img_gray)
cv2.waitKey(0)

# apply binary threshold
# adjust threshold from 50 to 150 to get good results for the corresponding image
ret, img_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
# display the image
cv2.imshow('Binary Image', img_thresh)
cv2.waitKey(0)

# detect contours on binary image
contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# draw contours on original image
img_copy = image.copy()
cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2, lineType=cv2.LINE_AA)

# display the image
cv2.imshow('Contour Image', img_copy)
cv2.waitKey(0)

cv2.destroyAllWindows()
