FROM python:3.9.6 as dev

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

FROM dev as build

COPY . .

CMD ["flask" "run"]