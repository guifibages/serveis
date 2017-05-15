#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libcnml import CNMLParser
import requests
import sys

def parse(raw_cnml):
    c = CNMLParser(raw_cnml)
    return c

def request_cnml_from_zone(zone):
    return requests.get('https://guifi.net/en/guifi/cnml/%d/detail' % zone).text

def save_cnml(data):
    fn = '/tmp/cnml.xml'
    with open(fn, 'w+') as f:
        f.write(data)
    return fn

def is_supernode(node):
    for device in node.get_devices():
        for interface in device.get_interfaces():
            for link in interface.get_links():
                if link.type != 'ap/client':
                    return True
    return False

if __name__ == '__main__':
    zone = 2426 # bages

    raw_cnml = request_cnml_from_zone(zone)
    filename = save_cnml(raw_cnml)
    p = parse(filename)
    
    for node in p.get_nodes():
        if is_supernode(node):
            print(node)
            for dev in node.get_devices():
                print(dev, dev.mainipv4)
                html = requests.get(dev.mainipv4).text
                if 'RouterOS' in html:
                    print('Mikrotik')
