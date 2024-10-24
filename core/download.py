from typing import Any
import urllib.request
from urllib.request import Request

def download(url) -> Any:
    return urllib.request.urlopen(url).decode('utf-8')

def handle_binary(url, filename):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req).read()
    print(type(response))
    save(response, filename, mode="wb")

def save(text, filename, mode="w"):
    with open(file=filename, mode=mode) as file:
        file.write(text)

def handle(url, filename):
    text = download(url)

    save(text, filename, mode="w")

def extract_file_name(url: str) -> str:
    return url.split("/")[-1]
