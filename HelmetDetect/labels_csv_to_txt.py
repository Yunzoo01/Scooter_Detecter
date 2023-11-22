import os
import glob

# 이미지 파일과 레이블 파일이 있는 디렉터리 경로
data_dir = "data"

# YOLO 형식의 레이블로 변환된 데이터를 저장할 디렉터리 경로
output_dir = "open-images-v6/validation/labels"

# 클래스 매핑
class_mapping = {
    "/m/0cmf2": 0,
    "/m/02wbm": 1,
    "/m/02xwb": 2,
    # 다른 클래스에 대한 매핑도 추가할 수 있습니다.
}

# 이미지의 너비와 높이
image_width = 1.0  # 예시로 1.0으로 설정
image_height = 1.0  # 예시로 1.0으로 설정

# 변환된 레이블 저장 디렉터리
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 레이블 데이터를 YOLO 형식으로 변환하여 저장
with open("open-images-v6/validation/labels/detections.csv", "r") as f:
    lines = f.readlines()
    for line in lines[1:]:  # 헤더 행 제외
        parts = line.strip().split(",")
        label_name = parts[2]
        class_id = class_mapping.get(label_name, -1)
        if class_id == -1:
            continue

        x_min, x_max, y_min, y_max = map(float, parts[4:8])
        x_center = (x_min + x_max) / 2 / image_width
        y_center = (y_min + y_max) / 2 / image_height
        width = (x_max - x_min) / image_width
        height = (y_max - y_min) / image_height

        yolo_label = f"{class_id} {x_center} {y_center} {width} {height}"

        # 이미지 파일 이름과 일치하는 YOLO 레이블 파일에 저장
        image_id = parts[0]
        label_file_name = os.path.join(output_dir, f"{image_id}.txt")
        with open(label_file_name, "a") as label_file:
            label_file.write(yolo_label + "\n")
