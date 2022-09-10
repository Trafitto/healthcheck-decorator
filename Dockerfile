FROM python:3.8
ADD . /code
WORKDIR /code
ENTRYPOINT ["python"]
CMD ["python"]