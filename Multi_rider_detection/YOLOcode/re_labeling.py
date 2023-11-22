# 0이 alone_rider
# 1이 multi_rider

import os

# 라벨링 txt 파일이 저장된 디렉터리 경로
label_directory = 'yolov5/Scooter/train/Multi_rider_labels' # 실제 경로로 변경하세요.

for filename in os.listdir(label_directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(label_directory, filename)
        with open(filepath, 'r') as file:
            lines = file.readlines()

        with open(filepath, 'w') as file:
            for line in lines:
                labels = line.split()
                # 라벨 변경
                if labels[0] == '0':
                    labels[0] = '1'
                elif labels[0] == '1':
                    labels[0] = '0'
                # 변경된 라벨로 파일 쓰기
                file.write(' '.join(labels) + '\n')
