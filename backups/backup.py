#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import socket
import os
import re
import shutil

class AbstractDeviceBackup(object):

    def __init__(self, remote, username, password):
        (hostname, port) = remote
        self.remote = remote
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args):
        self.close()
        
    def connect(self):
        raise NotImplementedError('')
    
    def backup(self, fullpath):
        raise NotImplementedError('')

    def close(self):
        raise NotImplementedError('')

class MikrotikBackup(AbstractDeviceBackup):

    def connect(self):
        sshclient = paramiko.SSHClient()
        sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshclient.connect(self.hostname, self.port, self.username, self.password)
        sshclient.exec_command("export file=plaintext.backup")
        sshclient.close()
        
        t = paramiko.Transport(self.remote)
        t.connect(None, self.username, self.password)
        self.sftp = paramiko.SFTPClient.from_transport(t)
        self.t = t

    def files2backup(self):
        return [re.compile(".*\.backup$"), re.compile(".*\.rsc$")]

    def match(self, fn):
        for pattern in self.files2backup():
            if pattern.match(fn):
                return True

        return False

    def backup(self, destination):
        for f in self.sftp.listdir('/'):
            if not self.match(f):
                continue
            
            with self.sftp.open(os.path.join('/', f), 'rb') as fo:
                with open(os.path.join(destination, f), 'wb+') as fd:
                    fd.write(fo.read())

    def close(self):
        self.sftp.close()
        self.t.close()
    
if __name__ == '__main__':
    backup_path = '/backup'

    hostname = '192.168.88.1'
    port = 22
    remote = (hostname, port)
    username = 'admin'
    password = ''

    path = os.path.join(backup_path, '%s' % hostname)

    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

    with MikrotikBackup(remote, username, password) as mb:
        mb.backup(path)
