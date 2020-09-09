FROM ubuntu:latest
RUN apt-get update -y
#RUN apt-get install python3 -y
RUN apt-get install python3 -y

RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install Flask==1.0.2
ENTRYPOINT ["python"]
CMD ["app.py"]
