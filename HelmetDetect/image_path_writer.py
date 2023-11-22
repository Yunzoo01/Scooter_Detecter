from glob import glob
import yaml
import torch.nn as nn  # nn 모듈 추가

# 이미지 경로 가져오기
train_img_list = glob('yolov5/helmet/train/images/*.jpg')
test_img_list = glob('yolov5/helmet/test/images/*.jpg')
valid_img_list = glob('yolov5/helmet/valid/images/*.jpg')
print(len(train_img_list), len(test_img_list), len(valid_img_list))

# 경로 파일 저장
with open('yolov5/helmet/train.txt', 'w') as f:
    f.write('\n'.join(train_img_list) + '\n')

with open('yolov5/helmet/test.txt', 'w') as f:  # 수정: 중복되는 슬래시 제거
    f.write('\n'.join(test_img_list) + '\n')

with open('yolov5/helmet/val.txt', 'w') as f:  # 수정: 중복되는 슬래시 제거
    f.write('\n'.join(valid_img_list) + '\n')


data_content = """
train: ./helmet/train/images
test: ./helmet/test/images  
val: ./helmet/valid/images  

nc: 2
names: ['With Helmet', 'Without Helmet']
"""

with open('yolov5/helmet/data.yaml', 'w') as file:
    file.write(data_content)

with open('yolov5/helmet/data.yaml', 'r') as file:
    content = file.read()
print(content)


# YAML 파일에서 클래스 수 가져오기
with open("yolov5/helmet/data.yaml", 'r') as stream:
    num_classes = yaml.safe_load(stream)['nc']

# 템플릿 설정
template = f"""
# Parameters
nc: {num_classes}  # number of classes (클래스 수 설정)
depth_multiple: 0.33  # model depth multiple
width_multiple: 0.50  # layer channel multiple
anchors:
  - [10, 13, 16, 30, 33, 23]  # P3/8
  - [30, 61, 62, 45, 59, 119]  # P4/16
  - [116, 90, 156, 198, 373, 326]  # P5/32

# YOLOv5 v6.0 backbone
backbone:
  # [from, number, module, args]
  [[-1, 1, Conv, [64, 6, 2, 2]],  # 0-P1/2
   [-1, 1, Conv, [128, 3, 2]],  # 1-P2/4
   [-1, 3, C3, [128]],
   [-1, 1, Conv, [256, 3, 2]],  # 3-P3/8
   [-1, 6, C3, [256]],
   [-1, 1, Conv, [512, 3, 2]],  # 5-P4/16
   [-1, 9, C3, [512]],
   [-1, 1, Conv, [1024, 3, 2]],  # 7-P5/32
   [-1, 3, C3, [1024]],
   [-1, 1, SPPF, [1024, 5]],  # 9
  ]

# YOLOv5 v6.0 head
head:
  [[-1, 1, Conv, [512, 1, 1]],
   [-1, 1, nn.Upsample, [None, 2, 'nearest']],
   [[-1, 6], 1, Concat, [1]],  # cat backbone P4
   [-1, 3, C3, [512, False]],  # 13

   [-1, 1, Conv, [256, 1, 1]],
   [-1, 1, nn.Upsample, [None, 2, 'nearest']],
   [[-1, 4], 1, Concat, [1]],  # cat backbone P3
   [-1, 3, C3, [256, False]],  # 17 (P3/8-small)

   [-1, 1, Conv, [256, 3, 2]],
   [[-1, 14], 1, Concat, [1]],  # cat head P4
   [-1, 3, C3, [512, False]],  # 20 (P4/16-medium)

   [-1, 1, Conv, [512, 3, 2]],
   [[-1, 10], 1, Concat, [1]],  # cat head P5
   [-1, 3, C3, [1024, False]],  # 23 (P5/32-large)

   [[17, 20, 23], 1, Detect, [nc, anchors]],  # Detect(P3, P4, P5)
  ]
"""

# 파일로 저장
with open("yolov5/models/custom_yolov5s.yaml", "w") as file:
    file.write(template.strip())  # 앞뒤 공백 제거 후 저장

# 해당 파일 내용 출력
with open("yolov5/models/custom_yolov5s.yaml", 'r',  encoding='ISO-8859-1') as file:
    print(file.read())