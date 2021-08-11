FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev
RUN apt update && apt install -y libsm6 libxext6
RUN apt install libgl1-mesa-glx -y
WORKDIR /RevisionImagnes
COPY . /RevisionImagnes
RUN pip3 --no-cache-dir install Pillow
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone
RUN apt-get update && \
    apt-get install -y zbar-tools
RUN pip3 install -r requirements.txt
ENV DEBIAN_FRONTEND=noninteractive 
RUN sudo apt install tesseract-ocr
RUN sudo apt-get install tesseract-ocr-spa
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1
CMD ["python3","reviewImg.py"]
