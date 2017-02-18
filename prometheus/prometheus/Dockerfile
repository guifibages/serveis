FROM golang:1.7-wheezy

RUN GO15VENDOREXPERIMENT=1 go get github.com/prometheus/prometheus/cmd/...
RUN apt-get update && apt-get install build-essential libsnmp-dev snmp-mibs-downloader && \
    GO15VENDOREXPERIMENT=1 go get github.com/prometheus/snmp_exporter/...

# FROM prom/prometheus:v1.5.2

# ENV SNMP_EXPORTER_VERSION=0.2.0

# RUN cd /tmp && \
#     git clone "https://github.com/prometheus/snmp_exporter/archive/v$SNMP_EXPORTER_VERSION" && \
#     unzip "v$SNMP_EXPORTER_VERSION.zip" && \
#     cd snmp_exporter-$SNMP_EXPORTER_VERSION && \
#     go get -d && \
#     go build
