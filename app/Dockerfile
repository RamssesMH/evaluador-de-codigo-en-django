FROM python:3.9

ARG user
ARG uid

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install docker docker-compose -y

ENV SECRET_KEY=""
ENV DATABASE_NAME=""
ENV DATABASE_USER=""
ENV DATABASE_PASSWORD=""
ENV DATABASE_HOST=""
ENV DATABASE_PORT=3306


ADD run.sh /code
RUN chmod +x run.sh

RUN mkdir /app
WORKDIR /app

RUN useradd $user -u $uid -s /bin/bash

RUN chown -R $user /code
RUN chmod -R 500 /code 
RUN chown -R $user /app
RUN gpasswd -a $user docker
# RUN (echo soptec1035; echo soptec1035) | passwd $user
#USER $user

CMD /bin/bash -c '/code/run.sh' && /bin/bash
