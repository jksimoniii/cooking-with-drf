FROM nginx

ARG FRONTEND_HOST=titan.dev.expandshare.com
ARG FRONTEND_PORT=80
ARG BACKEND_HOST=local.myproj.expandshare.com
ARG BACKEND_PORT=8000
ARG PROXY_PORT=80
ENV DOLLAR=$

ADD ./proxy.conf /etc/nginx/conf.d/proxy.conf
RUN env
RUN cat /etc/nginx/conf.d/proxy.conf
RUN envsubst </etc/nginx/conf.d/proxy.conf > /etc/nginx/conf.d/proxy_temp.conf
RUN mv /etc/nginx/conf.d/proxy_temp.conf /etc/nginx/conf.d/proxy.conf
RUN cat /etc/nginx/conf.d/proxy.conf
