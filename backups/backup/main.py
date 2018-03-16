#!/usr/bin/env python
from list import get_supernodes
from classify import classify

import asyncio
import aiohttp


async def main():
    while True:
        for ipv4 in get_supernodes(2426):  # supernodes al bages
            device_type = await classify(ipv4)
            async with aiohttp.ClientSession() as session:
                async with session.post(f'http://dns-api:5000/dns/record/all.guifinet/3600/A/{ipv4}',
                                        headers={"Content-Type": "application/json"}) as response:
                    print(await response.text())

                async with session.post(f'http://dns-api:5000/dns/record/{device_type}-device.guifinet/3600/A/{ipv4}',
                                        headers={"Content-Type": "application/json"}) as response:
                    print(await response.text())
        
        print("Will sleep for 3600s")
        await asyncio.sleep(3600)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
