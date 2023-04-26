import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("D:/Program/OpenCV/DeepFace/Practice/trained_model/version1/model.h5")
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, frame = cap.read()
    frame = frame[50:500, 50:500, :]
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(frame, (120, 120))
    resized = np.expand_dims(resized, 0)
    
    prediction = model.predict(resized/255)
    sample_cord = prediction[1][0]
    
    if (prediction[0]) > 0.5:
        cv2.rectangle(frame,
                  (int(sample_cord[0]*450)+15, int(sample_cord[1]*450)),
                  (int(sample_cord[2]*450)+15, int(sample_cord[3]*450)),
                  (255,0, 0), 1)
        cv2.putText(frame, 'Face', 
                    (int(sample_cord[0]*450), int(sample_cord[1]*450 - 5)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA 
                    )
        
    cv2.imshow('Face Tracker', frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    