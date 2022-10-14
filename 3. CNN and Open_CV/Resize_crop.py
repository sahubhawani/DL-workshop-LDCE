import cv2

#Resize the images

img = cv2.imread("/home/sagar/Test_Images/cricket.jpg")
print(img.shape)

resized_image = cv2.resize(img,(300,200))
print(resized_image.shape)

#Cropping of the images
cropped_image = img[0:200, 200:600]

cv2.imshow("Image",img)
cv2.imshow("Resized_image",resized_image)
cv2.imshow("Cropped_image",cropped_image)

if cv2.waitKey(0) & 0xff == ord('q'):
    destroyAllWindows()