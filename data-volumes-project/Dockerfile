FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

ARG DEFAULT_PORT=80

ENV PORT $DEFAULT_PORT

EXPOSE $PORT

CMD ["npm", "start"]

# docker build -t feedback-node:1.0 --build-arg DEFAULT_PORT=8000 .
# create container with volumes for feedback storage (persistent) and node_modules
# docker run -d --rm -p 3000:80 --env PORT=8000 --name feedback-app -v feedback:/app/feedback -v "C:\Users\LP\Documents\VS Projects\docker-notebook\data-volumes-project:/app" -v /app/node_modules mounted:v1

# note that on windows you need to be in WSL2 subsystem have nodemon refreshing server on file changes