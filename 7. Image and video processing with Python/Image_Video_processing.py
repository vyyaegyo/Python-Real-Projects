# Loading, displaying and resizing
import cv2

img=cv2.imread("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/7. Image and video processing with Python/galaxy.jpg", 0) #in -1, 1 color chanel and 0 is in gray scale
print(type(img)) #numpy.ndarray

resized_image= cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy", img)
cv2.imwrite("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/7. Image and video processing with Python/Galaxy_resized.jpg", resized_image)
cv2.waitKey(0) #specify the time of window will be closed in miliseconds
cv2.destroyAllWindows() #method to close the window

# Detects faces in images
import cv2

face_cascade=cv2.CascadeClassifier("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/7. Image and video processing with Python/haarcascade_frontalface_default.xml")

img=cv2.imread("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/7. Image and video processing with Python/photo.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img, 
      scaleFactor=1.05,
      minNeighbors=5)

for x, y, w, h in faces:
    img=cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0),3)

print(type(faces))
print(faces)

resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Capture
import cv2
import time

a =0 # number of iteration during recording the video

video=cv2.VideoCapture(1)

while True:
    a=1+1
    check, frame = video.read()
    print(check)
    print(frame)
    #time.sleep(3)
    cv2.imshow("Capturing", frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()