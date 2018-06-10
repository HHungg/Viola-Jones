import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture('E:/Program Files/Download/Adele - Hello.mp4')
count = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    count = count + 1

    if(count%60 == 1):
	    # Our operations on the frame come here
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	    for (x,y,w,h) in faces:

	    	frameCrop = frame[y:y+h,x:x+w]
	    	if(h > 100 and w > 100):
	    		faceCrop = cv2.resize(frameCrop, (32,32))
	    		cv2.imwrite("img/face"+str(count)+".jpg", faceCrop)

	    	# cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	    	# roi_gray = gray[y:y+h, x:x+w]
	    	# roi_color = frame[y:y+h, x:x+w]

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()