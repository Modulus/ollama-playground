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
