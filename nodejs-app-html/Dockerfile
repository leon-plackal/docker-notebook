FROM node

# execute subsequent commands in /app folder in container
WORKDIR /app

# copy package.json to /app folder in container (this is done first so that npm install is not run every time a file changes in the app)
COPY package.json /app

RUN npm install

COPY . /app

# expose port 80
EXPOSE 80

# command to run the app once the container is up
CMD ["node", "server.js"]

# build image with docker build -t <image-name>:tag .
## run container with docker run -p 3000:80 <image-name>