import os

# 탐지할 폴더 경로
image_folder_path = 'sample'

# 모델 weights 경로
weights_path = 'detection_models/Multi_passenger1.pt'

# 탐지 코드 실행
os.system(f'python yolov5/detect.py --weights {weights_path} --img 416 --conf 0.4 --source {image_folder_path} --view-img --save-txt')
