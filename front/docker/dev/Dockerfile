FROM node:12.18.4

WORKDIR /front

COPY ./.vscode ./.vscode
COPY ./public ./public
COPY ./src ./src
COPY ./jsconfig.json ./jsconfig.json
COPY ./package.json ./package.json
COPY ./yarn.lock ./yarn.lock

RUN yarn install

CMD ["yarn", "run", "start"]