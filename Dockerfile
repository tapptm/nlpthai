FROM python:3.9.10-alpine3.14

WORKDIR /srv

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r /tmp/requirements.txt

# RUN python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.14.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl

COPY . /srv

ENV FLASK_APP=app

CMD ["python3","app.py"]