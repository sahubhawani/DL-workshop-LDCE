import cv2
import numpy as np

#Contour and shape detection

def getContours(img):
    
    contours , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)[-2:]
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(img_contour, cnt , -1 , (255,0,0), 3)
        
        if area > 500:
            
            peri = cv2.arcLength(cnt,True)
#             print(peri)
            
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
#             print(approx)
            print(len(approx))
            
            objCor = len(approx)
            x , y , w , h = cv2.boundingRect(approx)
            
            cv2.rectangle(img_contour , (x,y),(x+w,y+h),(0,255,0),3)
            
            if objCor == 3: objType = "Tri"
            elif objCor == 4: objType = "Rect"
            elif objCor > 4 : objType = "Circle"
            else : objType = "None"
            
            
            cv2.putText(img_contour,objType , (x+(w//2),y+(h//2)),cv2.FONT_HERSHEY_COMPLEX, 0.5 ,(0,0,0),2 )


img = cv2.imread("/home/sagar/shapes_contour.jpg")

img_contour = img.copy()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur_img = cv2.GaussianBlur(gray_img,(7,7),1)

canny_img = cv2.Canny(blur_img,50,50)

blank_img = np.zeros_like(img)

getContours(canny_img)

cv2.imshow("Shapes_image",img)
cv2.imshow("Gray_image",gray_img)
cv2.imshow("Blur_image",blur_img)
cv2.imshow("Canny_image",canny_img)
cv2.imshow("Blank_image",blank_img)
cv2.imshow("Contour_image",img_contour)



if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()