# Task-4.2 : Take 2 image crop some part of both image and swap it. 

import cv2

# Display 1st image
img1 = cv2.imread("tiger.jpg")
img1 = cv2.resize(img1 , (600,450))

cv2.imshow("1st Image" , img1)
cv2.waitKey()
cv2.destroyAllWindows()

# Display 2nd image

img2 = cv2.imread("lion.jpg")
img2 = cv2.resize(img2 , (600,450))

cv2.imshow("2nd Image" , img2)
cv2.waitKey()
cv2.destroyAllWindows()

# Crop  1st image

c1 = img1[60:280 , 110:320]

cv2.imshow("cropped1" , c1)
cv2.waitKey()
cv2.destroyAllWindows()

# crop  2nd image

c2 = img2[60:280 , 110:320]

cv2.imshow("cropped2" , c2)
cv2.waitKey()
cv2.destroyAllWindows()

import numpy as np

# Swapping of images

c1 = np.copy(c1)
c2 = np.copy(c2)

img1[60:280 , 110:320]=c2
img2[60:280 , 110:320]=c1

# Display swapped image1

cv2.imshow("swapped1" , img1)
cv2.waitKey()
cv2.destroyAllWindows()

# Display swapped image2

cv2.imshow("swapped2" , img2)
cv2.waitKey()
cv2.destroyAllWindows()
