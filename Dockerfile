FROM python:3.8
ADD . /code
WORKDIR /code
CMD ["python", "./app.py"]