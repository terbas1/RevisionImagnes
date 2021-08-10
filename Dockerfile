FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev
RUN apt update && apt install -y libsm6 libxext6
RUN apt install libgl1-mesa-glx -y
WORKDIR /RevisionImagnes
COPY . /RevisionImagnes
RUN pip3 --no-cache-dir install Pillow
RUN pip3 install -r requirements.txt
CMD ["python3","reviewImg.py"]
