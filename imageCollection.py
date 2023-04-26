import os 
import time
import uuid
import cv2
def collectImage():
    images_path = os.path.join('data', 'images')
    number_images = 30
    cap = cv2.VideoCapture(0)
    for i in range(number_images):
        print(f"Image No {i} is being collected")
        res, frame = cap.read()
        imgname = os.path.join(images_path, f"{str(uuid.uuid1())}.jpg")
        print(imgname)
        # cv2.imwrite(filename = imgname, img=frame)
        # cv2.imshow("Captured Frames : ", frame)
        # time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()