from PIL import Image
import os

input_directory = 'yolov5/helmet/train/images'   # 이미지 파일들이 있는 디렉토리 경로
output_directory = 'yolov5/helmet/train/images2' # 변환된 JPG 파일들을 저장할 디렉토리 경로

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    # 파일 확장자가 .jpg가 아닌 경우만 변환
    if not filename.endswith('.jpg'):
        with Image.open(os.path.join(input_directory, filename)) as img:
            # 파일 이름에서 확장자 제거
            basename = os.path.splitext(filename)[0]
            img.save(os.path.join(output_directory, basename + '.jpg'))

print("All images have been converted to JPG!")
