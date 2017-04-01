# Prometheus

Aquesta carpeta conté els següents serveis:
 - **Prometheus**: recolectar les mètriques que han recollit els exporters
   - *_exporters: per recollir les dades dels *targets* (routers, antenes, ...) i unificar el format de les mètriques
   - alertmanager: s'encarrega d'enviar alertes segons les condicions configurades
 - Grafana: per visualitzar les dades que ha recollit Prometheus

## Posada en marxa

### Requisits

 - Docker (provat amb 17.03)
 - Docker Compose (1.8)

### Configuració

S'ha d'afegir a `prometheus/prometheus.yml` els *targets* d'on volem recollir les mètriques. Per exemple:

```
- job_name: 'snmp_routers'
  static_configs:
    - targets:
      - 10.228.16.129
      - ...
```

### Execució

```
cd serveis/prometheus
docker-compose up --build
``` 
