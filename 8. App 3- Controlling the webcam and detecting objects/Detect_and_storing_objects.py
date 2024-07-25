import cv2, time
import pandas as pd
from datetime import datetime

first_frame = None  #this code is applied for motion detection
status_list=[None,None]
times=[]
df=pd.DataFrame(columns=["Start","End"])

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0) #we want to blur the image

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status=1

        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    status_list.append(status)
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key=cv2.waitKey(1)
    print(gray)

    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

print(status_list) 
print(times)

for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]}, ignore_index=True)

df.to_csv("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/8. App 3- Controlling the webcam and detecting objects/Times.csv")

video.release()
cv2.destroyAllWindows()


