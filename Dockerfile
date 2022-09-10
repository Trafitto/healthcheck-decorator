FROM python:3.8
ADD . /code
WORKDIR /code
RUN pip install redis
CMD ["python", "./app.py"]