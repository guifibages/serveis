FROM alpine:latest

MAINTAINER Jordi Masip <jordi@masip.cat>

RUN apk --update add bind

EXPOSE 53

COPY config/ /etc/bind/
RUN chown -R named /etc/bind/

ENTRYPOINT ["named", "-c", "/etc/bind/named.conf", "-g", "-u", "named"]
