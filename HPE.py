import cv2 as cv
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# video feed
cap = cv.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    # with ~ as : 파일 or 함수를 열고 with 내부의 코드가 실행이 끝나면 닫힘 
    # 즉 with 내부에서는 pose를 이용해서 mediapipe 사용가능
    
    while cap.isOpened():
        ret, frame = cap.read() #ret: 비디오가 정상적으로 불러와졌는지
                                #frame : 실제 비디오 정보
                                
        # Detection
        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB) # cv는 비디오를 BGR로 받아오고 
                                                     # mediapipe는 RGB로 비디오를 다루기 때문에 변환해야함
        image.flags.writeable = False
        
        results = pose.process(image) # 실제로 관절 감지를 진행하는 부분
        
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        
        # 관절 그리기
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245,66,66), thickness=2, circle_radius=2)
                                    )
        # results.pose_landmarks 에 감지한 관절의 좌표가 저장되어 있다.
                                
        cv.imshow("Mediapipe feed", image)
        
        if cv.waitKey(1) == ord('q'): # q누르면 break
            break
        
    cap.release()
    cv.destroyAllWindows()


    
    

