import os
import time

# 작업 디렉터리 변경
os.chdir('yolov5')  # '/path/to/yolov5' 를 실제 YOLOv5 디렉터리 경로로 변경해주세요.

# 시간 측정 시작
start_time = time.time()

# 훈련 코드 실행 (배치 크기와 이미지 크기 조정)
os.system('python train.py --img 640 --batch 16 --epochs 100 --data ./helmet/data.yaml --cfg ./models/custom_yolov5s.yaml --weights "" --name helmet_results4 --cache')

# 학습된 모델을 사용하여 검증 세트의 성능 평가
os.system(f'python test.py --data ./helmet/data.yaml --weights runs/train/helmet_results4/weights/best.pt --img 640')

# 시간 측정 종료 및 출력
end_time = time.time()
print(f"Elapsed Time: {end_time - start_time} seconds")