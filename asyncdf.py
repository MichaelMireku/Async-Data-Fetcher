import asyncio
import aiohttp
import os
import argparse

async def fetch_data(url, headers=None):
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Raise an exception for HTTP errors
                return await response.text()
    except aiohttp.ClientError as e:
        return f"Error fetching data from {url}: {str(e)}"

async def save_to_file(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(data)
        print(f"Data saved to {filename}")
    except OSError as e:
        print(f"Error saving data to {filename}: {str(e)}")

async def main():
    parser = argparse.ArgumentParser(description="Async Data Fetcher")
    parser.add_argument('--urls', nargs='+', help='Space-separated list of URLs to fetch', required=True)
    parser.add_argument('--headers', nargs='+', help='Space-separated list of custom headers')
    parser.add_argument('--output-dir', help='Directory to save fetched data', default='output')

    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    headers = {header.split(':')[0]: header.split(':')[1] for header in args.headers} if args.headers else None

    tasks = [fetch_data(url, headers=headers) for url in args.urls]
    results = await asyncio.gather(*tasks)

    for i, result in enumerate(results, start=1):
        print(f"Data from URL-{i}:\n{result}\n{'='*30}\n")

        # Save each fetched data to a file
        filename = os.path.join(args.output_dir, f"data_from_url_{i}.txt")
        await save_to_file(result, filename)

if _name_ == "_main_":
    asyncio.run(main())