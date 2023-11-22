import cv2
import torch

# 3개의 YOLOv5 모델 로드
model1 = torch.hub.load('ultralytics/yolov5', 'custom', path='Helmet_best.pt')
model2 = torch.hub.load('ultralytics/yolov5', 'custom', path='Multi_passenger3.pt')
model3 = torch.hub.load('ultralytics/yolov5', 'custom', path='detection_models/Scooter_best.pt')
model1.eval()
model2.eval()
model3.eval()

video_path = 'Can Two People Ride on X9 Electric Scooter？.webm'
video = cv2.VideoCapture(video_path)

# 동영상의 프레임 크기를 얻기
frame_width = int(video.get(3))
frame_height = int(video.get(4))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video_three_model.avi', fourcc, 30.0, (frame_width, frame_height))

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # 첫 번째 모델의 결과 그리기
    combined_frame = model1(frame).render()[0]

    # 두 번째 모델의 결과 그리기
    combined_frame = model2(combined_frame).render()[0]

    # 세 번째 모델의 결과 그리기
    combined_frame = model3(combined_frame).render()[0]

    # 결과를 저장
    out.write(combined_frame)

    cv2.imshow('Output', combined_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()
