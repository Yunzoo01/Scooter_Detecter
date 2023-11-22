import os
import shutil

# 경로 정의
source_path = "add_data/labels"
destination_path = "yolov5/scooter/train/labels"

# augmented_images에 있는 모든 파일을 images로 이동
for file_name in os.listdir(source_path):
    source_file = os.path.join(source_path, file_name)
    destination_file = os.path.join(destination_path, file_name)
    shutil.move(source_file, destination_file)

# augmented_images 디렉토리 삭제
os.rmdir(source_path)
