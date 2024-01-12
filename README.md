# Async Data Fetcher

Async Data Fetcher is a Python script that performs asynchronous fetching of data from multiple URLs. It utilizes asyncio and aiohttp to efficiently handle concurrent network requests.

## Features

- Asynchronous data fetching from specified URLs
- Customizable headers for HTTP requests
- Saving fetched data to text files
- Command-line interface for user interaction

## Prerequisites

- Python installed (Python 3.7 or higher recommended)
- aiohttp library installed (pip install aiohttp)

## Usage

Run the script from the command line with the following options:

```bash
python asyncdf.py --urls <url1> <url2> --headers "Header1: Value1" "Header2: Value2" --output-dir <output_directory>