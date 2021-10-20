FROM continuumio/anaconda3:4.4.0

# WORKDIR /script


COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY /script .

CMD ["python", "main.py"]
