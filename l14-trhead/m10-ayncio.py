import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    
    for url, result in zip(urls, results):
        print(f"URL: {url}\nContent: {result}\n")

if __name__ == "__main__":
    asyncio.run(main())
