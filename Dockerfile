FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev
RUN apt update && apt install -y libsm6 libxext6
RUN apt install libgl1-mesa-glx -y
WORKDIR /RevisionImagnes
COPY . /RevisionImagnes
RUN pip3 --no-cache-dir install Pillow
ENV DEBIAN_FRONTEND=noninteractive 
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
CMD ["python3","reviewImg.py"]
