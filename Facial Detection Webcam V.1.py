import cv2

video_capture= cv2.VideoCapture(0, cv2.CAP_DSHOW)

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

a=0

while True:
    
    
    Check, frame = video_capture.read()
 
    Gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    
    faces=face_cascade.detectMultiScale(Gray,
                                    scaleFactor=1.1,
                                    minNeighbors=6)
    
    for x,y,w,h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    cv2.imshow("Window",frame)
    
    
    print(frame)
    a+=1
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Number of frames: {}".format(a))

video_capture.release()
cv2.destroyAllWindows()


