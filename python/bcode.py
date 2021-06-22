import numpy as np   
import cv2
import time
import sys
import json


# set up camera object
cap = cv2.VideoCapture(-1)

# QR code detection object
detector = cv2.QRCodeDetector()

while True:
    # get the image
    _, img = cap.read()
    # get bounding box coords and data
    data, bbox, _ = detector.detectAndDecode(img)
    
    # if there is a bounding box, draw one, along with the data
    if(bbox is not None):
        for i in range(len(bbox)):
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
                     0, 255), thickness=2)
        #image =np.zeros((512,512,3), np.uint8)
        #cv2.putText(image,data,(100,200), cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
        #cv2.imshow("image",image)
        
#         cv2.waitKey(5000)
        if data:
            info= {"camera": data}
            with open("js/bcode.json", "w") as write_file:
                json.dump(info, write_file)
                
            print(data)
            
            exit()
            #exec(open('get_MQTT_data.py').read())

    # display the image preview
    #cv2.imshow("code detector", img)
    if(cv2.waitKey(1) == ord("q")):
       break
# free camera object and exit
cap.release()
cv2.destroyAllWindows()
