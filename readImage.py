# Python code to read image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk
import __myFilters as mfs


# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread(
    "C:/Users/91990/OneDrive/Pictures/Wall/img1.jpg", cv2.IMREAD_COLOR)

# select ROI
showCrosshair = False
fromCenter = False
r = cv2.selectROI(img, fromCenter, showCrosshair)


# crop image
imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
img_gray = cv2.cvtColor(imCrop, cv2.COLOR_BGR2GRAY)
# grayImgArr = np.asarray(imCrop)

print(img_gray)
print(img_gray.size)
cv2.imshow("cropped image", img_gray)


# apply gaussian
gaussian_filtered_image = mfs.blur(imCrop)
cv2.imshow("blurred crop image", gaussian_filtered_image)


# plt.imshow(imCrop, cmap='gray')

# To hold the window on screen; cv2.waitKey method
cv2.waitKey(0)
