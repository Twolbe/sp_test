FROM node:12.18.4 as builder

WORKDIR /front

COPY ./.vscode ./.vscode
COPY ./public ./public
COPY ./src ./src
COPY ./jsconfig.json ./jsconfig.json
COPY ./package.json ./package.json
COPY ./yarn.lock ./yarn.lock

RUN yarn install
RUN yarn build

# целевой образ
FROM nginx

RUN rm -rf /usr/share/nginx/html/*
COPY ./docker/prod/nginx/conf.d /etc/nginx/conf.d
COPY --from=builder /front/build /usr/share/nginx/html

WORKDIR /etc/nginx

CMD ["nginx", "-g", "daemon off;"]
