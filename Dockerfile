FROM python:3

WORKDIR /ip

COPY . /ip

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/python3", "/ip/PythonApps/iplocator.py"]