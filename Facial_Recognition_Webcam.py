import cv2

video_capture= cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    
    Check, frame = video_capture.read()
 
    cv2.imshow("Window", frame)
    
    print(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
















