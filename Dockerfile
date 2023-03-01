FROM ubuntu
EXPOSE 4200:4200
WORKDIR base:/
COPY ./Version1/ base:/
RUN apt-get update && apt-get install -y nodejs python3
RUN apt-get update && npm install -g @angular/cli
RUN ng serve
#CMD ["ng serve"]
CMD ["cd", "static"]
CMD ["flask", "run"]