FROM python:3.12-slim

RUN apt-get -y update
RUN apt-get -y install build-essential
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "make", "run" ]