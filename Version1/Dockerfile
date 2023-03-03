FROM ubuntu:latest
EXPOSE 4200
EXPOSE 5000
WORKDIR /base
COPY package*.json ./ 
COPY . .

RUN apt-get update && apt-get install -y python3 curl
RUN apt remove -y nodejs nodejs-doc
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt install -y yarn


RUN apt-get update && apt install -y python3-pip
RUN pip install Flask
RUN pip install flask-restful 
RUN pip install flask-cors
RUN npm -f install
RUN npm -f install -g @angular/cli


#RUN ng serve
#RUN n
CMD ["/bin/bash", "-c", "./shellscript.sh"]

#CMD ["ng", "serve", "&"]
#CMD ["cd", "backend/static"]
#CMD ["flask", "run"]