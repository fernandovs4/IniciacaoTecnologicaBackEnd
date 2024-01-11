FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .



CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "app:app"]
