#!/usr/bin/env python3

import aiohttp
import asyncio
import fileinput
import async_timeout

async def fetch(url):
    try:
        async with aiohttp.ClientSession() as session:
            with async_timeout.timeout(10):
                async with session.get(url) as response:
                    return await response.text()
    except asyncio.TimeoutError:
        pass
    
    return None


async def detect_device(ipv4):
    text = await fetch('http://%s' % ipv4)
    if text:
        if text.contains('mikrotik'):
            return 'mikrotik'
    else:
        return 'unknown'


async def classify(ipv4):
    device = await detect_device(ipv4)
    print(ipv4, device, flush=True)
    return device

async def main(loop):
    ips = [line.strip() for line in fileinput.input()]
    futures = [asyncio.ensure_future(classify(ipv4)) for ipv4 in ips]
    asyncio.gather(*futures)
    print("done")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
