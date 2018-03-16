#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import asyncssh
import aiofiles
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

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        await self.close()
        
    def connect(self):
        raise NotImplementedError('')
    
    def backup(self, fullpath):
        raise NotImplementedError('')

    def close(self):
        raise NotImplementedError('')

class MikrotikBackup(AbstractDeviceBackup):
    
    async def connect(self):
        self.conn = await asyncssh.connect(self.hostname, port=self.port, username=self.username, password=self.password, known_hosts=None)

    async def backup(self, destination):
        # Generating backup file
        #result = await self.conn.run('export file=plaintext.backup', check=True)
        #result = await self.conn.run('ls', check=True)
        #print(result.stdout, end='')
        print("connected")

        return

        # Copying file
        async with conn.start_sftp_client() as sftp:
             async for f in await sftp.listdir('/'):
                 if self.match(f):
                     async with sftp.open(os.path.join('/', f), 'rb') as fo:
                         async with aiofiles.open(os.path.join(destination, f), mode='wb+') as fd:
                             await fd.write(await fo.read())

    async def close(self):
        await self.conn.close()

    def match(self, fn):
        files2backup = [re.compile(".*\.backup$"), re.compile(".*\.rsc$")]
        for pattern in files2backup:
            if pattern.match(fn):
                return True

        return False

async def main():
    backup_path = '/backup'

    hostname = '192.168.1.110'
    port = 22
    remote = (hostname, port)
    username = ''
    password = ''

    path = os.path.join(backup_path, '%s' % hostname)

    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

    async with MikrotikBackup(remote, username, password) as mb:
        await mb.backup(path)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
