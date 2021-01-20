FROM python:3

WORKDIR /ip

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

COPY PythonApps/webapp.py ./

EXPOSE 5000

#ENV FLASK_APP=webapp.py
#
#ENV FLASK_RUN_HOST=0.0.0.0
#
#ENTRYPOINT flask run

ENTRYPOINT ["/usr/local/bin/python3", "/ip/PythonApps/iplocator.py"]