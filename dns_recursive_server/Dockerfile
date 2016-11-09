FROM alpine:latest

MAINTAINER Jordi Masip <jordi@masip.cat>

RUN apk --update add bind

ENTRYPOINT ["named", "-c", "/etc/bind/named.conf", "-g", "-u", "named"]
