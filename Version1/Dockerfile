FROM ubuntu:latest
EXPOSE 4200
EXPOSE 5000
WORKDIR /Version1
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
RUN pip install Flask flask-restful flask-cors chess torch numpy
RUN npm -f install -g npm@9.5.1
RUN npm -f install -g @angular/cli


CMD ./shellscript.sh
# RUN flask --app ./backend/static/app run &


# RUN /bin/bash -c './frontend/shellscript.sh'

#RUN ng serve
#RUN n
# CMD ["/bin/bash", "-c", "cd ./frontend; ng serve"]
# CMD ["/bin/bash", "-c", "shellscript.sh"]
#CMD ["ng", "serve", "&"]
#CMD ["cd", "backend/static"]
#CMD ["flask", "run"]
