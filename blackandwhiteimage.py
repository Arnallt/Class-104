import numpy as np
import cv2

canvas = np.zeros([500,500])

canvas[150:250,100:400] = 255

cv2.imshow("Image", canvas)
cv2.waitKey(0)