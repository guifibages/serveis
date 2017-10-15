#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests
import sys

from libcnml import CNMLParser

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
            logging.debug('Node: %s' % node)
            for dev in node.get_devices():
                logging.debug('%s: %s' % (dev, dev.mainipv4))
                if len(dev.mainipv4) > 0:
                    print(dev.mainipv4)
