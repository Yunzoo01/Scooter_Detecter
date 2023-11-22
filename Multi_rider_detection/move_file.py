import shutil
import os

#a>b
source_folder = "yolov5/Scooter/train/Multi_rider_labels"  # 파일을 이동할 원본 폴더
destination_folder = "yolov5/Scooter/train/labels"  # 파일을 이동할 대상 폴더

# 원본 폴더 내의 모든 파일 리스트 가져오기
file_list = os.listdir(source_folder)

# 원본 폴더의 모든 파일을 대상 폴더로 이동
for file_name in file_list:
    source_file = os.path.join(source_folder, file_name)
    destination_file = os.path.join(destination_folder, file_name)
    shutil.move(source_file, destination_file)

print("모든 파일을 이동했습니다.")
