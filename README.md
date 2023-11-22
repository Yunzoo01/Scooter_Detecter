# Scooter_Detecter
###### This project is still in progress. I wanted to create an AI model that detects scooters within cctv, but the YOLOv5 I used was not enough to detect small objects within CCTV. So I first created an AI model that detects large objects. I'm going to re-project using Faster R-CNN with higher accuracy.
##### This project is a project to create AI models using YOLOv5. I made AI that detects whether a driver is wearing a helmet or not, and detects if there are more than one driver. I also created an AI model that detects scooters because I aimed to detect them within CCTV. The data set is not included in the code.

## 🌻Features
- Detecting if the driver is wearing a helmet(Helmet_best.pt)
- Detecting two or more drivers(Multi_passenger3.pt)
- Detecting scooters (Scooter_best.pt)

## 🌻Project Environment
- Python Version : Python 10
- Development IDE : PyCharm 2023 Community Edition
- Frameworks and Tools :
  - YOLOv5 : Utilized for object detection, acquired from its GitHub repository.
  - LabelImg : Used for image annotation, downloaded from its GitHub repository.
- Operating System :
  - Initial development on Windows.
  - Subsequent development and testing on Kali Linux.

## 🌻Application Screenshot
### ▪️ Labeling
![image](https://github.com/Yunzoo01/Scooter_Detecter/assets/116542699/dda8b80f-2448-48d8-a37b-70244ff1bd0c)
### ▪️ Failed Image
![image](https://github.com/Yunzoo01/Scooter_Detecter/assets/116542699/fb43daf1-eaba-419d-8eb9-d18924d6a094)
### ▪️ Result Image
#### There is a video in the code file that tested the model.
![image](https://github.com/Yunzoo01/Scooter_Detecter/assets/116542699/89ccd19a-ab46-4355-9486-2a655b4d31da)
![image](https://github.com/Yunzoo01/Scooter_Detecter/assets/116542699/22674920-c94f-4d5f-9fe2-973161f76f26)
