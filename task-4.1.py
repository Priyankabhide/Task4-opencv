# Task 4.1 - Create image by yourself Using Python Code 

import cv2
import numpy as np

canvas = np.zeros((720,750,3))

# stairs
cv2.rectangle(canvas , (260,600) , (465,140), [255,255,255], -1)
cv2.rectangle(canvas , (280,580) , (446,130), [0,255,0], -1)

# Door & window
cv2.rectangle(canvas , (200,200) , (620,550) , [255,0,0] , -1)
cv2.rectangle(canvas , (300,300) , (430,550), [200,0,255] , -1)
cv2.rectangle(canvas , (470,300) , (580,400), [255,255,255], -1)

# roof
cv2.rectangle(canvas , (520,50) , (570,145), [255,255,255], -1)

# Triangle roof
p1 = (410,20)
p2 = (140,200)
p3 = (680,200)

cont = np.array( [p1, p2, p3] )

cv2.circle(canvas, p1, 2, (200,0,255), 1)
cv2.circle(canvas, p2, 2, (200,0,255), 1)
cv2.circle(canvas, p3, 2, (200,0,255), 1)

cv2.drawContours(canvas, [cont], 0, (200,0,255), -1)

cv2.imshow("Happy HOME",canvas)
cv2.waitKey()
cv2.destroyAllWindows()
