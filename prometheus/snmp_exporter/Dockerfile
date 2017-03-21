FROM quay.io/prometheus/busybox:latest

COPY snmp_exporter  /bin/snmp_exporter

EXPOSE      9116
ENTRYPOINT  [ "/bin/snmp_exporter" ]
CMD         [ "-config.file=/etc/snmp_exporter/snmp.yml" ]
