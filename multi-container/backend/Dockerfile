FROM node

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . .

EXPOSE 80

ENV MONGODB_USERNAME=username
ENV MONGODB_PASSWORD=password

CMD ["node", "app.js"]