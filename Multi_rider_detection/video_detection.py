import cv2
import torch

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/Scooter_results43/weights/best.pt')  # 'path'를 사용하여 모델을 로드
model.eval()

video_path = 'Can Two People Ride on X9 Electric Scooter？.webm'
video = cv2.VideoCapture(video_path)

# 동영상의 프레임 크기를 얻기
frame_width = int(video.get(3))
frame_height = int(video.get(4))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video1.avi', fourcc, 30.0, (frame_width, frame_height))

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # YOLOv5 모델을 프레임에 적용
    results = model(frame)

    # 결과를 이미지에 그리기
    results_img = results.render()  # 변경된 부분
    output_frame = results_img[0]  # 변경된 부분

    # 비디오에 쓰기
    out.write(output_frame)

    cv2.imshow('Output', output_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()
