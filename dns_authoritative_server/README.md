# DNS autoritatiu de guifibages.cat

Aquesta carpeta conté les receptes per posar en marxa la mínima expressió d'un servidor BIND9 sobre Docker. S'ha verificat el correcte funcionament amb Docker 1.12.3 i Docker Compose 1.8.1.

## Posada en marxa

Primer de tot cal instal·lar **Docker** (seguir les instruccions a https://docs.docker.com/engine/installation/) i **Docker Compose** (`pip install docker-compose`).

Aquests són els passos per posar-ho en marxa:

```bash
# Primer de tot cal clonar aquest repositori a la màquina que farà de servidor de DNS.
git clone git@github.com:guifibages/serveis.git
cd serveis

# Afegir a la carpeta "zones" els fitxers de cada zona
...

# Afegir al fitxer "named.conf" per definir cada una de les zones que es troba a la carpeta "zones".
...

# Posar en marxa la instància del servidor
docker-compose up # afegir "-d" per executar en mode dimoni

# Obtenir la IP de la instància
docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress }}' $(docker ps -aq) | grep "dns"

# Verificar el correcte funcionament (s'espera la ip 1.2.3.4)
dig @<instance-ip> test.example.local
```

## Generar claus TSIG

L'objectiu d'aquest apartat és generar una clau compartida entre un DNS *master* i un *slave* per autenticar els missatge que intercanvien. 

Per generar la clau compartida cal escollir un nom, per exemple, `host1-host2.` o bé `master-salve.`:

```bash
ddns-confgen -q -k master-slave. > master-slave.key
```

`master-slave.key`:
```
key "master-slave." {
	algorithm hmac-sha256;
	secret "0m0n7GqtxZTPc0...y3r8z236VY=";
};
```

Creem un fitxer anomenat `named.conf.tsigkeys` que es trobarà a ambdós servidors de DNS, master i esclau. Contindrà el contingut de `master-slave.key`.

Finalment, fem un `include` del fitxer `named.conf.tsigkeys` a `named.conf`:

```
...
include "/etc/bind/zones/example.conf";

include "/etc/bind/named.conf.tsigkeys";
```

Per verificar el correcte funcionament:
```bash
dig @ip-dns-master qualsevol.domini.cat -k master-slave.key
```
