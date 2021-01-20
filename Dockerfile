FROM python:3

WORKDIR /ip

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT FLASK_APP=/ip/PythonApps/webapp.py flask run --host=0.0.0.0

#ENTRYPOINT ["/usr/local/bin/python3", "/ip/PythonApps/iplocator.py"]