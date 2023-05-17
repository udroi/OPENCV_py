# import required libraries
import cv2
import numpy as np
import tkinter as tk
import __myFilters as mfs

# read input image
img = cv2.imread('C:/Users/91990/OneDrive/Pictures/Wall/img1.jpg')

# define transformation matrix
m = np.ones((3, 3))


# apply the cv2.transform to perform matrix transformation
img_tr = cv2.transform(img, m, None)

print(img_tr)

# display the transformed image
cv2.imshow("Transformed Image", img_tr)


blr_img = mfs.blur(img_tr)
cv2.imshow("blurred Image", blr_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
