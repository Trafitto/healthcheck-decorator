FROM python:3.11
ADD . /code
WORKDIR /code
ENTRYPOINT ["python"]
CMD ["python"]