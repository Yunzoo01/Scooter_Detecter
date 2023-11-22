import os

# 라벨링이 저장된 디렉터리 경로
label_dir = "yolov5/helmet8/valid/labels"

for filename in os.listdir(label_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(label_dir, filename), 'r') as file:
            lines = file.readlines()
            new_lines = []

            for line in lines:
                # 첫 번째 문자는 라벨을 나타냄 (예: "0 0.5 0.5 1 1" 또는 "1 0.5 0.5 1 1")
                label = line[0]
                if label == '0':
                    new_lines.append('1' + line[1:])
                elif label == '1':
                    new_lines.append('0' + line[1:])

        # 수정된 라벨로 파일을 다시 저장
        with open(os.path.join(label_dir, filename), 'w') as file:
            file.writelines(new_lines)

print("All labels have been updated!")
