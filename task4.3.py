# Task 4.3 
# Take images and combine them to form a single image (collage) 

import cv2

# Read and display 1st image
p1 = cv2.imread("ML.jpg")
p1 = cv2.resize(p1, ([300, 300]))

cv2.imshow('ML', p1)
cv2.waitKey()
cv2.destroyAllWindows()

# Read and Display 2nd image
p2 = cv2.imread("Docker.jpeg")
p2 = cv2.resize(p2, ([300, 300]))

cv2.imshow('Docker', p2)
cv2.waitKey()
cv2.destroyAllWindows()

# Read and Display 3rd image
p3 = cv2.imread("Flutter.png")
p3 = cv2.resize(p3, ([300, 300]))

cv2.imshow('Flutter', p3)
cv2.waitKey()
cv2.destroyAllWindows()

# Read and Display 4th image 
p4 = cv2.imread("AWS.jpg")
p4 = cv2.resize(p4, ([300, 300]))

cv2.imshow('AWS', p4)
cv2.waitKey()
cv2.destroyAllWindows()

# Now we have to attach image with other image
# First we have to create a horizontal stack of images
# And add it to the vertical stack
# Let the horizontal pair be (p1,p2) and (p3,p4)
import numpy

horizontal1 = numpy.hstack([p1, p2])
horizontal2 = numpy.hstack([p3, p4])

# Now the horizontal attachment is done
# And now we have to do vertical attachment
vertical = numpy.vstack([horizontal1, horizontal2])
vertical = cv2.resize(vertical, ([600, 550]))

# Final Attachment
cv2.imshow('Final-Collage', vertical)
cv2.waitKey()
cv2.destroyAllWindows()
# TASK COMPLETED !!!
