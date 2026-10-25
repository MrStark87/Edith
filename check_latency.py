# VPS se latency check:  python check_latency.py
# MongoDB aur Telegram API ka response time (ms) batata hai.
import asyncio
import statistics
import time

import httpx
from pymongo import AsyncMongoClient

from misskaty.vars import BOT_TOKEN, DATABASE_URI


async def main():
    client = AsyncMongoClient(DATABASE_URI)
    await client.admin.command("ping")  # connection warm-up
    times = []
    for _ in range(10):
        t = time.perf_counter()
        await client.admin.command("ping")
        times.append((time.perf_counter() - t) * 1000)
    print(f"MongoDB   : avg {statistics.mean(times):.0f} ms | min {min(times):.0f} | max {max(times):.0f}")

    times = []
    async with httpx.AsyncClient(timeout=20) as http:
        for _ in range(5):
            t = time.perf_counter()
            await http.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getMe")
            times.append((time.perf_counter() - t) * 1000)
    print(f"Telegram  : avg {statistics.mean(times):.0f} ms | min {min(times):.0f} | max {max(times):.0f}")
    print("\nMongoDB 50 ms se upar ho to DB bot se door hai (region alag). Neeche padho.")


asyncio.run(main())
