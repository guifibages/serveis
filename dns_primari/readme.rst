-----------------------
DNS Autoritatiu Primari
-----------------------

.. image:: https://github.com/allusa/serveis/workflows/DNS%20primari/badge.svg
    :target: https://github.com/allusa/serveis/workflows/DNS%20primari/badge.svg



Configuració
------------

Totes les zones a `conf`_.

* Cal escriure tots els serials com a `2017100101` perquè siguin canviats dinàmicament.



Execució
--------

`docker-compose up`


Es pot configurar el serial a `docker-compose.yaml`_::

 - serial=2020010101


Instal·lar eines addicionals per a debugar:

* `apk --update add bind-tools`


CI/CD
-----

Mitjançant Github Actions en el fitxer `dnsprimari.yml`_.

#https://github.com/actions/starter-workflows/blob/master/ci/docker-publish.yml


Producció
---------

TODO

docker swarm init?



.. _conf: conf
.. _docker-compose.yaml: docker-compose.yaml
.. _dnsprimari.yml: ../.github/workflows/dnsprimari.yml
