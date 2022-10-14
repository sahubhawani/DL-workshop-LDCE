import cv2

import numpy as np

#Joining Images

img = cv2.imread("/home/sagar/Test_Images/cricket.jpg")

horImg = np.hstack((img,img))

verImg = np.vstack((img,img))

cv2.imshow("Horizontal",horImg)

cv2.imshow("Vertical",verImg)

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()

#Make sure while stacking the images must be of same dimessions.