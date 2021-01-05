FROM python:3

RUN pip3 install -r requirements.txt

WORKDIR /ip

COPY . /ip

ENTRYPOINT ["/usr/local/bin/python3", "/ip/PythonApps/iplocator.py"]