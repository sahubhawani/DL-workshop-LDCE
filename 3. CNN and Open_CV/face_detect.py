import cv2

#Detecting Faces with cascades defined in OpenCv

facecascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")


img = cv2.imread("/home/sagar/face.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = facecascade.detectMultiScale(gray_img , 1.1,4)

for (x , y, w , h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Face",img)
cv2.imshow("Gray image",gray_img)

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()