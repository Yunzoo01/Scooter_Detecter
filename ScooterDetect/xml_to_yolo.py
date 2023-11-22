import os
import xml.etree.ElementTree as ET


def convert_annotation(xml_folder, txt_outfolder, class_names):
    if not os.path.exists(txt_outfolder):
        os.makedirs(txt_outfolder)

    list_xml_files = os.listdir(xml_folder)
    for xml_file in list_xml_files:
        if xml_file.endswith('.xml'):
            in_file = open(os.path.join(xml_folder, xml_file), 'r', encoding='utf-8')
            out_file_name = xml_file[:-4] + '.txt'
            out_file = open(os.path.join(txt_outfolder, out_file_name), 'w')
            tree = ET.parse(in_file)
            root = tree.getroot()

            img_width = int(root.find('size/width').text)
            img_height = int(root.find('size/height').text)

            for obj in root.iter('object'):
                difficult = obj.find('difficult').text
                cls = obj.find('name').text
                if cls not in class_names or int(difficult) == 1:
                    continue
                cls_id = class_names.index(cls)
                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text),
                     float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text))
                bb = ((b[0] + b[2]) / 2.0) / img_width, ((b[1] + b[3]) / 2.0) / img_height, \
                     (b[2] - b[0]) / img_width, (b[3] - b[1]) / img_height
                out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

            in_file.close()
            out_file.close()

# 클래스 이름 목록을 지정합니다. ['Scooter']로 지정했습니다.
class_names = ['Scooter']
convert_annotation('추가데이터라벨링', '추가데이터라벨링', class_names)
