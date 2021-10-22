FROM  python

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY /script .

CMD tail -f /dev/null
