import urllib.request


def download(url):
    return urllib.request.urlopen(url).read().decode('utf-8')

def save(text, filename):
    with open(file =filename, mode="w") as file:
        file.write(text)

def handle(url, filename):
    text = download(url)
    save(text, filename)


handle(url="https://www.gutenberg.org/cache/epub/16/pg16.txt", filename="peterpan.txt")