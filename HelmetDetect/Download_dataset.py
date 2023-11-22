import os
import urllib.request
import zipfile

# 데이터를 저장할 디렉터리 생성
output_dir = "yolov5/helmet10"
os.makedirs(output_dir, exist_ok=True)

# 데이터 다운로드 및 압축 해제
download_url = "https://universe.roboflow.com/ds/cR2ezdnV5h?key=T44ccnMcD6"
downloaded_file = os.path.join(output_dir, "roboflow.zip")

urllib.request.urlretrieve(download_url, downloaded_file)

with zipfile.ZipFile(downloaded_file, 'r') as zip_ref:
    zip_ref.extractall(output_dir)

# 다운로드된 zip 파일 삭제
os.remove(downloaded_file)
