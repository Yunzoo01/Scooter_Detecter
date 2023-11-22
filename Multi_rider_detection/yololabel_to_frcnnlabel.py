import os
import xml.etree.ElementTree as ET
from PIL import Image

def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.width, img.height

def convert_yolo_to_xml(yolo_file_path, image_dir, output_dir, classes):
    try:
        image_filename = os.path.basename(yolo_file_path).replace('.txt', '.jpg')
        image_path = os.path.join(image_dir, image_filename)
        image_width, image_height = get_image_size(image_path)

        root = ET.Element("annotation")
        ET.SubElement(root, "folder").text = os.path.basename(image_dir)
        ET.SubElement(root, "filename").text = image_filename
        ET.SubElement(root, "path").text = image_path

        source = ET.SubElement(root, "source")
        ET.SubElement(source, "database").text = "Unknown"

        size = ET.SubElement(root, "size")
        ET.SubElement(size, "width").text = str(image_width)
        ET.SubElement(size, "height").text = str(image_height)
        ET.SubElement(size, "depth").text = "3"

        ET.SubElement(root, "segmented").text = "0"

        with open(yolo_file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5:
                    class_id, x_center, y_center, width, height = map(float, parts)
                    x_min = int((x_center - width / 2) * image_width)
                    y_min = int((y_center - height / 2) * image_height)
                    x_max = int((x_center + width / 2) * image_width)
                    y_max = int((y_center + height / 2) * image_height)

                    object = ET.SubElement(root, "object")
                    ET.SubElement(object, "name").text = classes[int(class_id)]
                    ET.SubElement(object, "pose").text = "Unspecified"
                    ET.SubElement(object, "truncated").text = "0"
                    ET.SubElement(object, "difficult").text = "0"

                    bndbox = ET.SubElement(object, "bndbox")
                    ET.SubElement(bndbox, "xmin").text = str(x_min)
                    ET.SubElement(bndbox, "ymin").text = str(y_min)
                    ET.SubElement(bndbox, "xmax").text = str(x_max)
                    ET.SubElement(bndbox, "ymax").text = str(y_max)
                else:
                    print(f"Skipping line due to incorrect format: {line}")
                    continue

        tree = ET.ElementTree(root)
        xml_output_path = os.path.join(output_dir, image_filename.replace('.jpg', '.xml'))
        tree.write(xml_output_path)

    except Exception as e:
        print(f"Error processing file {yolo_file_path}: {e}")

def convert_all_yolo_files(yolo_dir, image_dir, output_dir, classes):
    os.makedirs(output_dir, exist_ok=True)
    processed_count = 0
    error_count = 0

    for filename in os.listdir(yolo_dir):
        if filename.endswith('.txt'):
            try:
                yolo_file_path = os.path.join(yolo_dir, filename)
                convert_yolo_to_xml(yolo_file_path, image_dir, output_dir, classes)
                processed_count += 1
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
                error_count += 1

    print(f"Completed processing with {processed_count} files converted and {error_count} errors.")

# 클래스 이름 리스트 (실제 데이터셋에 맞게 수정 필요)
classes = ["alone_rider", "multi_rider"]

# 사용자의 디렉토리 구조에 맞게 경로 설정 필요
yolo_labels_dir = "/home/user/PycharmProjects/Multi_rider_detection/yolov5/Scooter/valid/labels"
yolo_images_dir = "/home/user/PycharmProjects/Multi_rider_detection/yolov5/Scooter/valid/images"
output_xml_dir = "/home/user/PycharmProjects/Multi_rider_detection/Faster-RCNN/valid/annotations"

# 모든 YOLO 라벨 파일을 XML로 변환 실행
convert_all_yolo_files(yolo_labels_dir, yolo_images_dir, output_xml_dir, classes)
