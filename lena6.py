import cv2
lenna=cv2.imread("lenna.bmp")
cv2.imshow("demo1",lenna)
cv2.imshow("demo2",lenna)
cv2.waitKey()
cv2.destroyAllWindows