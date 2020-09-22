FROM ubuntu:18.04

MAINTAINER Michael Cain "chsyone@aol.com"

RUN apt-get update -y && apt-get install -y python3-pip python3-dev

CMD ["ufg allow 5000"]

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY ./myAPI.py /app

ENTRYPOINT ["python3"]

CMD ["myAPI.py"]