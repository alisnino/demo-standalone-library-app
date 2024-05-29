FROM node:20.11.1 as dev

WORKDIR  /app

FROM dev as build

COPY package.json ./

RUN npm install

COPY . .

RUN npm run build

CMD ["npm", "start"]