import os

# 탐지할 폴더 경로
image_folder_path = 'sample'

# 모델 weights 경로
weights_path = 'yolov5/runs/train/helmet_results32/weights/best.pt'

# 탐지 코드 실행
os.system(f'python yolov5/detect.py --weights {weights_path} --img 416 --conf 0.4 --source {image_folder_path} --view-img --save-txt')