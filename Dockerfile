FROM python:3.8
ADD . /code
WORKDIR /code
RUN pip install redis
RUN pip install pytest
CMD ["python", "./app.py"]