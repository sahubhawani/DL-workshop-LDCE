import cv2

#Warping the images
import numpy as np

img = cv2.imread("/home/sagar/Warp_image_box.jpg")



width , height = 350,250

pts1 = np.float32([[328,480],[534,484],[338,782],[540,916]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])


matrix = cv2.getPerspectiveTransform(pts1,pts2)

warped_image = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Warped Image",warped_image)

if cv2.waitKey(0) & 0xff == ord('q'):

    cv2.destroyAllWindows()

# 338,782
# 540,916
# 328,480
# 534,484