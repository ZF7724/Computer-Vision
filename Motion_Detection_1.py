import cv2

first_frame=None

video_capture= cv2.VideoCapture(0, cv2.CAP_DSHOW)



while True:
    
    
    Check, frame = video_capture.read()
 
    Gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    Gray=cv2.GaussianBlur(Gray,(21,21),0)
    
    if first_frame is None:
        first_frame=Gray
        continue

    delta_frame=cv2.absdiff(first_frame,Gray)
        
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)
    
    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for countour in cnts:
        if cv2.contourArea(countour) <1000:
            continue
        
        (x,y,w,h)=cv2.boundingRect(countour)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
        
    
    
    #print(frame)
    #print(Gray)
    #print(delta_frame)
    print(thresh_frame)
    
    cv2.imshow("RGB frame",frame)
    cv2.imshow("Delta frame",delta_frame)
    cv2.imshow("Threshold frame",thresh_frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

