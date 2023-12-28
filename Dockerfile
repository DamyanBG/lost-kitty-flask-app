FROM python:3.10.8-bullseye

WORKDIR /flask-be-api

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w" , "4", "-b", "0.0.0.0", "main:app"]