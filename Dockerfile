FROM ubuntu:20.04
RUN apt-get update && apt-get install -y  python3-pip
WORKDIR /app
COPY  app.py test_app.py requirements.txt  ./
ADD  templates /app/templates
RUN pip install -r requirements.txt
RUN pip install -U pytest


CMD [ "python3" ,"app.py" ]
