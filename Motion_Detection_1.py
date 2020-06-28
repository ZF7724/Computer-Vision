import cv2
import datetime
import pandas

first_frame=None

video_capture= cv2.VideoCapture(0, cv2.CAP_DSHOW)
timing=[None,None]
status_list=[None,None]
df=pandas.DataFrame(columns=["Start","End"])



while True:
    
    
    Check, frame = video_capture.read()
    
    status=0
 
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
        if cv2.contourArea(countour) <10000:
            continue
        status=1
        
        (x,y,w,h)=cv2.boundingRect(countour)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
        
    status_list.append(status)
    
    
    
    if status_list[-1]==1 and status_list[-2]==0:
        timing.append(datetime.datetime.now())
        
    if status_list[-1]==0 and status_list[-2]==1:
        timing.append(datetime.datetime.now())
        
        
        
    #print(frame)
    #print(Gray)
    #print(delta_frame)
    print(thresh_frame)
    print(timing)
    
    cv2.imshow("RGB frame",frame)
    cv2.imshow("Delta frame",delta_frame)
    cv2.imshow("Threshold frame",thresh_frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        if status==1:
            timing.append(datetime.datetime.now())
        break
    
print(status)
print(status_list)

for i in range(0,len(timing),2):
    df=df.append({"Start":timing[i],"End":timing[i+1]},ignore_index=True)
    
    
df.to_csv("Motion_Times.csv")

video_capture.release()
cv2.destroyAllWindows()

