FROM python:3

RUN pip3 install requests

WORKDIR /apps

COPY . /apps

CMD ["python", "David.py", "-i", "1.1.1.1", "8.8.8.8"]