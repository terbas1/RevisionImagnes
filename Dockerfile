FROM alpine:3.14
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip
WORKDIR /RevisionImagnes
COPY . /RevisionImagnes
RUN pip3 install -r requirements-txt
CMD ["python3","RevisionImagnes/reviewImg.py"]