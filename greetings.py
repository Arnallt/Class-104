import cv2

img = cv2.imread("poster.jpg")
rocket = img[120:360, 400:500]

img[0:240,200:300] = rocket
text = "Poster"
cv2.putText(img,text,(200,50), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale= 1, color=(0,0,0))
cv2.imwrite("Greetings.jpg", img)
cv2.imshow("Display", img)
cv2.waitKey(0)