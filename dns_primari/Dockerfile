FROM alpine:latest
MAINTAINER guifibages

RUN apk --update add bind bind-tools

COPY conf /etc/bind
# canvia serials
ARG serial=2017102701
RUN sed -i -e "s/2017100101/${serial}/g" $(find /etc/bind -type f)

EXPOSE 53
CMD ["named", "-c", "/etc/bind/named.conf", "-g", "-u", "named"]