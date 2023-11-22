import os
import shutil

# A-2와 B-2 폴더의 경로 설정
a2_dir = "yolov5/Scooter/valid/Alone_rider_labels"
b2_dir = "yolov5/Scooter/valid/Multi_rider_labels"

# C 폴더의 경로 설정
c_dir = "../yolov5/Scooter/valid/labels"

# A-1 폴더의 경로 설정 (하드 코딩)
a1_dir = "yolov5/Scooter/valid/Alone_rider_images"

# B-1 폴더의 경로 설정 (하드 코딩)
b1_dir = "yolov5/Scooter/valid/Multi_rider_images"

# A-2 폴더 내의 txt 파일을 A-2 폴더로 이동
for root, _, files in os.walk(c_dir):
    for file in files:
        if file.endswith(".txt"):  # txt 파일인지 확인
            txt_path = os.path.join(root, file)
            image_file_name = file.replace(".txt", ".jpg")  # 이미지 파일 이름 생성

            # 이미지 파일 이름이 A-1 폴더에 있는 경우, A-2 폴더로 이동
            if os.path.exists(os.path.join(a1_dir, image_file_name)):
                shutil.move(txt_path, os.path.join(a2_dir, file))

            # 이미지 파일 이름이 B-1 폴더에 있는 경우, B-2 폴더로 이동
            elif os.path.exists(os.path.join(b1_dir, image_file_name)):
                shutil.move(txt_path, os.path.join(b2_dir, file))
