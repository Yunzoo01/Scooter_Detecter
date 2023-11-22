import os

# 경로 정의
images_path = "yolov5/scooter/train/images"

# images 디렉토리에 있는 파일 수 계산
file_count = len([f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))])

print(f"There are {file_count} files in the 'images' directory.")
