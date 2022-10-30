import cv2
import winsound

classifier=cv2.CascadeClassifier(r'C:\Users\user\Documents\Python Scripts\Machine Learning\Computer Vision\Vehicle Counter\cars.xml')

video = cv2.VideoCapture(0)
counter=0
frequency = 1800
duration = 100 
while 1:

    ret,frame=video.read()
    
    
    height,width=frame.shape[0:2]
    
    cv2.putText(frame,'Count :',(10,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(247, 2, 162),2)
    cv2.line(frame,(0,height-150),(width,height-150),(247, 2, 26),2)
    
    blur=cv2.blur(frame,(3,3))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    vehicles = classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
    
    for (x,y,w,h) in vehicles:
        
        cars = int(y+h/2)
        line = height-150
        
        if(cars<line+8 and cars>line-8):
            
            counter=counter+1
            winsound.Beep(frequency, duration)

        cv2.rectangle(frame,(x,y),(x+w,y+h),(26, 2, 247),2)
        cv2.putText(frame,str(counter),(500,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(247, 2, 162),2)
        
    cv2.imshow('Real_Time-Vehicle_Counter',frame)
    key=cv2.waitKey(1)
    
    if key == ord('0'):
        break

cv2.destroyAllWindows()
video.release()