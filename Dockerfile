FROM alpine:3.14
WORKDIR /RevisionImagnes
COPY . /RevisionImagnes
RUN pip install -r requirements-txt
CMD ["python3","RevisionImagnes/reviewImg.py"]