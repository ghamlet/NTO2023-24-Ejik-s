import cv2
import os
import numpy as np

minblue, mingreen, minred, maxblue, maxgreen, maxred = 0, 0, 0, 255, 255, 255

change_image = False

dir_images = 'foto' 
path = "video_2024-02-25_18-15-02.mp4"


def nothing():
    ...


def trackbar(minblue=0, mingreen=0, minred=0, maxblue=0, maxgreen=0, maxred=0):

    cv2.namedWindow( "result")
    cv2.createTrackbar('minb', 'result', minblue, 255, nothing)
    cv2.createTrackbar('ming', 'result', mingreen, 255, nothing)
    cv2.createTrackbar('minr', 'result', minred, 255, nothing)
    cv2.createTrackbar('maxb', 'result', maxblue, 255, nothing)
    cv2.createTrackbar('maxg', 'result', maxgreen, 255, nothing)
    cv2.createTrackbar('maxr', 'result', maxred, 255, nothing)

    state = True
    return state


cap = cv2.VideoCapture(path)

while True:
    res, frame_input =  cap.read()
    if not res:
        break

    frame_input = cv2.resize(frame_input, (500,400))

    if not change_image:
        change_image = trackbar(minblue, mingreen, minred, maxblue, maxgreen, maxred) #create trackbars
    
        
    # img = os.listdir(dir_images)[pos]
    # frame_input = f"foto/{img}"
    # frame_input = cv2.imread(frame_input)

    hsv = cv2.cvtColor(frame_input, cv2.COLOR_BGR2HSV)
    color_tone_input = hsv[:,:,0]
    color_tone_input = np.sum(color_tone_input)

    minb = cv2.getTrackbarPos('minb', 'result')
    ming = cv2.getTrackbarPos('ming', 'result')
    minr = cv2.getTrackbarPos('minr', 'result')
    maxb = cv2.getTrackbarPos('maxb', 'result')
    maxg = cv2.getTrackbarPos('maxg', 'result')
    maxr = cv2.getTrackbarPos('maxr', 'result')


    mask = cv2.inRange(hsv,(minb,ming,minr),(maxb,maxg,maxr))
    #mask = cv2.inRange(hsv,(88,95,154),(117,255,255))
    result = cv2.bitwise_and(frame_input,frame_input,mask=mask)


    ret, thresh = cv2.threshold(mask, 127, 255, 0)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100] 
    bboxes = [cv2.boundingRect(cnt) for cnt in contours] 
    cv2.drawContours(frame_input, contours, -1, (255,0,255), 3)

    for i,(x,y,w,h) in enumerate(bboxes):
        cv2.rectangle(frame_input,(x,y),(x+w,y+h),(255,0,255),2) 
        cv2.putText(frame_input,str(i),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 0,255),2)




    cv2.imshow('result', result)
    cv2.imshow('frame_input', frame_input)
    cv2.imshow('mask', mask)

    k = cv2.waitKey(100)
    if k == ord('q'):
        break

    elif k == ord('s'):
        with open('trackbars/trackbars_save.txt', "a") as f:
            f.write(f"{minb, ming, minr}, {maxb, maxg, maxr}" +"\n")
    
    