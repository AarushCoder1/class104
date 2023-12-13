import cv2

img = cv2.imread("poster.jpg")

#cv2.imshow("Output", img)
#cv2.waitKey(0)


rocket = img[120:360, 400:500]
img[0:240, 500:600] = rocket


text_to_show = "I love coding at white hat jr"
cv2.putText(img, text_to_show, (20, 220), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0,0,255))
cv2.imshow("Output", img)
cv2.waitKey(0)