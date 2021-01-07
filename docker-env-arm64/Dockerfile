FROM nvcr.io/nvidia/l4t-ml:r32.4.4-py3

ENV PYTHONUNBUFFERED=0

RUN apt-get update &&\
    pip3 install paho-mqtt &&\
    pip3 install --ignore-installed PyYAML &&\
    pip3 install Flask
