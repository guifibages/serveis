# Servidor NTP basat en un receptor GPS

Aquesta carpeta conté les receptes per posar un servidor NTP sobre Docker. S'ha verificat el correcte funcionament amb Docker 1.12.3 i Docker Compose 1.8.1.

## Posada en marxa

Primer de tot cal instal·lar **Docker** (seguir les instruccions a https://docs.docker.com/engine/installation/) i **Docker Compose** (`pip install docker-compose`).

Aquests són els passos per posar-ho en marxa:

```bash
# Primer de tot cal clonar aquest repositori a la màquina que farà de servidor de NTP.
git clone git@github.com:guifibages/serveis.git
cd serveis

cd ntp_server

# Connectar el receptor GPS a l'ordinador i verificar:
cat /dev/ttyACM0

# Posada en marxa del servidor NTP
docker-compose up -d

# Obtenir la IP de la instància
docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress }}' $(docker ps -aq) | grep "ntpd"

# Verificar el correcte funcionament
ntpdate -q <instance-ip>
```
