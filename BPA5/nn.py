import cv2


config_path = "BPA5/cfg/yolov4-tiny-obj.cfg"  
weights_path = "BPA5/backup/yolov4-tiny-obj_final.weights" 
classes = ["people"]

def find_people(frame):
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

    yolo_model = cv2.dnn.DetectionModel(net)
    yolo_model.setInputParams(size= (416,416), scale= 1/255, swapRB=True)


    class_ids, scores, boxes = yolo_model.detect(frame, 0.2, 0.2)

    if len(class_ids):
        print("Detect people")
        
        for id in class_ids:
            print(classes[id])

        for box in boxes:
            (x,y,w,h) = box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("people", frame)
        cv2.waitKey(10)
        return True


    