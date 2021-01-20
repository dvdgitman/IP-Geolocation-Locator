FROM python:3

WORKDIR /ip

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

COPY PythonApps/webapp.py ./

EXPOSE 5000

ENV api_key=45c974ed84mshc94c890bbd503ffp1d0eb4jsn218473e78459

ENTRYPOINT FLASK_APP=./webapp.py flask run -i 1.1.1.1 8.8.8.8 --host=0.0.0.0

#ENTRYPOINT ["/usr/local/bin/python3", "/ip/PythonApps/iplocator.py"]