FROM python:3

RUN pip3 install requests

WORKDIR /ip

COPY . /ip

ENTRYPOINT ["/usr/local/bin/python3", "/ip/iplocator.py"]