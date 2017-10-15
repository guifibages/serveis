#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aiohttp
import asyncio
import backup
import fileinput

async def fetch(url):
    print("fetch")
    async with aiohttp.ClientSession(loop=loop) as session:
        with aiohttp.Timeout(10, loop=session.loop):
            async with session.get(url) as response:
                 return await response.text()
    return None

async def detect_device(ipv4):
    try:
        text = await fetch('http://%s' % ipv4)
        if text.contains('mikrotik'):
            return 'mikrotik'
    except asyncio.TimeoutError:
        pass
    
    return 'unknown'

async def start_backup(ipv4):
    print("Backup")
    device = await detect_device(ipv4)
    print(ipv4, device, flush=True)
    await backup.main()

async def main(loop):
    futures = []
    for line in fileinput.input():
        ipv4 = line.strip()
        futures += [asyncio.ensure_future(start_backup(ipv4), loop=loop)]

    print("endfor")

    for future in futures:
        await future
        print("done")
    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
