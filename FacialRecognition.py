import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


Image=cv2.imread("Face Picture.jpg")
grey_image=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)


faces=face_cascade.detectMultiScale(grey_image,
                                    scaleFactor=1.1,
                                    minNeighbors=6)
for x,y,w,h in faces:
    Image=cv2.rectangle(Image,(x,y),(x+w,y+h),(0,255,0),3)


print(faces)
print(type(faces))

resized=cv2.resize(Image,(int(Image.shape[1]/3),int(Image.shape[0]/3)))


cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()



















