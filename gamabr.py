import cv2
import sys
# do instal  modul opencv-python

image = cv2.imread("gambar.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayImageInv = 255 - grayImage
grayImageInv = cv2.GaussianBlur(grayImageInv, (21, 21), 0)
output = cv2.divide(grayImage, 255-grayImageInv, scale = 256.0)
resizeImg = cv2.resize(output, (int(h/2), int(w/2)))
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("pencilsketch", cv2.WINDOW_AUTOSIZE)
cv2.imshow("image", image)
cv2.imshow("pencilsketch", resizeImg)
#
cv2.imrite("save_pencilsketch", output)
cv2.waitKey()
cv2.destroyAllWindows()
