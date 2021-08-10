FROM python3.8-alpine3.13
RUN apk add --no-cache python4-dev \
    && pip3 install --upgrade pip
WORKDIR /RevisionImagnes
COPY . /RevisionImagnes
RUN pip install -r requirements-txt
CMD ["python3","RevisionImagnes/reviewImg.py"]