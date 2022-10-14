import cv2

img = cv2.imread("/home/sagar/Test_Images/cricket.jpg")

#Converting image into gray scale
gray_image = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

#Converting gray scale image into blurred image
blur_image = cv2.GaussianBlur(gray_image, (7,7),0)

#Edge detection by Canny edge detector
canny_image = cv2.Canny(img ,300,300)

#Dilation of the image to make edges more significant
import numpy as np
kernel = np.ones((5,5),np.uint8) #kernel required for dilation process swip 
dilation_image = cv2.dilate(canny_image, kernel,iterations = 1 )

#Errosion of the image
erroded_image = cv2.erode(dilation_image , kernel , iterations = 1)


cv2.imshow("Gray_Image",gray_image)

cv2.imshow("Blur_Image",blur_image)

cv2.imshow("Canny_Image",canny_image)

cv2.imshow("Dilated_Image",dilation_image)

cv2.imshow("Erroded_Image",erroded_image)


if cv2.waitKey(0) & 0xff == ord('s'):
    destroyAllWindows()