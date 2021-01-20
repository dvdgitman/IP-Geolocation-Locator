FROM python:3

WORKDIR /ip

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

COPY PythonApps/webapp.py ./PythonApps

EXPOSE 5000

ENV api_key="45c974ed84mshc94c890bbd503ffp1d0eb4jsn218473e78459"

#ENV FLASK_APP=webapp.py
#
#ENV FLASK_RUN_HOST=0.0.0.0
#
#ENTRYPOINT flask run

ENTRYPOINT ["/usr/local/bin/python3", "/ip/PythonApps/iplocator.py"]