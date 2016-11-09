# DNS recursiu

Aquesta carpeta conté les receptes per posar en marxa la mínima expressió d'un servidor BIND9 sobre Docker. S'ha verificat el correcte funcionament amb Docker 1.12.3 i Docker Compose 1.8.1.

## Posada en marxa

Primer de tot cal instal·lar **Docker** (seguir les instruccions a https://docs.docker.com/engine/installation/) i **Docker Compose** (`pip install docker-compose`).

Aquests són els passos per posar-ho en marxa:

```bash
# Primer de tot cal clonar aquest repositori a la màquina que farà de servidor de DNS.
git clone git@github.com:guifibages/serveis.git

cd serveis/dns_recursive_server

# Modificar la configuració del servidor a "named.conf" per definir com s'ha de comportar el servidor
...

# Posar en marxa la instància del servidor
docker-compose up # afegir "-d" per executar en mode dimoni

# Obtenir la IP de la instància
docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress }}' $(docker ps -aq) | grep "dns"

# Verificar el correcte funcionament
dig @<instance-ip> guifi.net
```
