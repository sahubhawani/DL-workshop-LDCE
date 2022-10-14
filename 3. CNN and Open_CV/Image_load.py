import cv2

#Reading from images
img = cv2.imread("/home/sagar/Test_Images/cricket.jpg")
cv2.imshow("Output",img)
if cv2.waitKey(0) & 0xff ==ord("q"):
    cv2.destroyAllWindows()
