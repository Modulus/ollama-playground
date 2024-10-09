# Pdf
chuck the text after extracting it.

Overlapping chuncks.

embedding the text -> vector database with dimensions

kan store chunks in json file locally, but not recommended.

You need to store both the chunks and the source text.

Make sure you use a model that supports embedding



## Embeddings api

/api/embeddings < deprecrated

/v1/embeddings -> openapi compatible (please do not use, unless you really NEEED it!

/api/embed < use this
----
Example use of /api/embed
```

{
    model: "nomic-embed-text",
    input: "embedding is fun"
}
```


## Open web ui --> I could not get this to work


To use RAG, the following steps worked for me (I have LLama3 + Open WebUI v0.3.5 Docker container):

    I copied a file.txt from my computer to the Open WebUI container:
    $ docker cp ~/Downloads/file.txt open-webui:/app/backend/data/docs/

    In the Open WebUI Admin Panel > Settings > Documents > Scan for documents from DOCS_DIR (/data/docs), I clicked Scan. It confirmed with Scan complete!

    I refreshed the New Chat page with CTRL+R.

    In the prompt, I typed the hashtag # key, it listed the scanned files, I selected file.txt, I asked a question about it, for example "what does the context contain?" , and it answered correctly about the contents of the file.


# RAG course youtube
https://www.youtube.com/watch?v=V1Mz8gMBDMo