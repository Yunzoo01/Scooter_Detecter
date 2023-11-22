import os

folder_path = "yolov5/Scooter/train/Multi_rider_images"  # 파일을 검사할 폴더의 경로

# 폴더 내의 모든 파일 리스트 가져오기
file_list = os.listdir(folder_path)

# 조건을 만족하는 파일을 삭제
for file_name in file_list:
    if len(file_name) >= 3 and file_name[:3] in ['pqr']:
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)

print("파일을 삭제했습니다.")
