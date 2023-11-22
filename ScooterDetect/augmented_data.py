import cv2
import os
import albumentations as A

# 데이터셋 경로
dataset_path = "add_data"
images_path = os.path.join(dataset_path, "images")
labels_path = os.path.join(dataset_path, "labels")

# 증강된 이미지 및 레이블을 저장할 경로 생성
augmented_images_path = os.path.join(dataset_path, "augmented_images")  # 이미지 저장 경로
augmented_labels_path = os.path.join(dataset_path, "augmented_labels")  # 레이블 저장 경로

if not os.path.exists(augmented_images_path):
    os.makedirs(augmented_images_path)

if not os.path.exists(augmented_labels_path):
    os.makedirs(augmented_labels_path)

# 증강을 위한 변환 정의
transform = A.Compose([
    A.ToGray(p=0.2),  # 흑백 이미지로 변환
    A.HorizontalFlip(p=0.5),  # 좌우 반전
    A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=0.2),  # RGB 시프트
    A.ChannelShuffle(p=0.2),  # 채널 섞기
    A.GridDistortion(p=0.2),  # 그리드 왜곡
    A.ElasticTransform(alpha=1, sigma=50, alpha_affine=50, p=0.2),  # 탄성 변형
    A.GaussNoise(var_limit=(10.0, 50.0), p=0.2),  # 가우시안 노이즈 추가
    A.Cutout(num_holes=8, max_h_size=32, max_w_size=32, p=0.2),  # 이미지에서 부분 삭제

    # 다른 증강 방식 추가 가능
], bbox_params=A.BboxParams(format='yolo', label_fields=['labels']))


# 이미지와 레이블을 동시에 증강
for img_file in os.listdir(images_path):
    image = cv2.imread(os.path.join(images_path, img_file))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, _ = image.shape

    txt_file = img_file.replace(".jpg", ".txt")
    with open(os.path.join(labels_path, txt_file), 'r') as f:
        lines = f.readlines()
        bboxes = []
        labels = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) % 5 != 0:  # 각 bounding box에는 5개의 값이 있으므로, 전체 값의 개수는 5의 배수여야 합니다.
                print("Unexpected line format:", line)
                continue
            for i in range(0, len(parts), 5):  # 5개씩 값을 가져와서 처리합니다.
                label, x_center, y_center, width, height = map(float, parts[i:i + 5])

                # width와 height가 너무 큰 경우, 이를 보정합니다.
                if x_center + width / 2 > 1.0:  # x_max를 검사
                    width = 2 * (1.0 - x_center)
                if y_center + height / 2 > 1.0:  # y_max를 검사
                    height = 2 * (1.0 - y_center)

                if 0.0 <= x_center <= 1.0 and 0.0 <= y_center <= 1.0 and 0.0 <= width <= 1.0 and 0.0 <= height <= 1.0:
                    bboxes.append([x_center, y_center, width, height])
                    labels.append(int(label))
                else:
                    print(f"Warning: Invalid bounding box values detected - {parts[i:i + 5]}")

    augmented = transform(image=image, bboxes=bboxes, labels=labels)
    augmented_image = augmented['image']
    augmented_bboxes = augmented['bboxes']
    augmented_labels = augmented['labels']

    # 증강된 이미지 저장
    aug_img_file = os.path.join(augmented_images_path, f"d_" + img_file)
    cv2.imwrite(aug_img_file, cv2.cvtColor(augmented_image, cv2.COLOR_RGB2BGR))

    # 증강된 레이블 저장
    aug_txt_file = os.path.join(augmented_labels_path, f"d_" + txt_file)
    with open(aug_txt_file, 'w') as f:
        for bbox, label in zip(augmented_bboxes, augmented_labels):
            x_center, y_center, width, height = bbox
            f.write(f"{label} {x_center} {y_center} {width} {height}\n")
