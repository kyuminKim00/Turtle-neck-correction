# Turtle-neck-correction
자세유지, 거북목 교정 프로그램

open-cv, mediapipe, pyguiauto

<img width="320" alt="pose_landmarks_index" src="https://github.com/kyuminKim00/Turtle-neck-correction/assets/112574294/28796f50-6735-4106-bf0e-8300f598b13a">


정면의 웹캠을 이용해서 얻은 컴퓨터 사용자의 현재 자세를 HPE(Human pose estimation)로 감지한다.
사용자의 어깨 관절, 얼굴의 좌표를 계산할 수 있고 이 좌표를 바탕으로 정면에서 봤을 때 코와 어깨 사이의 거리, 각도 등을 계산한 후 일정 범위, 시간 이상으로 안좋은 자세가 유지되면 사용자에게 알림을 준다.

체형은 사용자마다 모두 다르기 때문에 좋은 자세의 기준은 처음 프로그램을 시작할 때 사용자가 의도적으로 10초동안 유지한 올바른 자세를 기준으로 잡는다.

