from typing import List
from pypdf import PdfReader
import functools

from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunkify(file: str, size=100, overlap=10) -> List[str]:
    text_list = extract_text_from_pdf(file)

    print(len(text_list))

    doc = functools.reduce(lambda x, y: x + y, text_list)
    doc = " ".join(doc.split()) # Remove all newlines and tabs

    print(doc.count("\n"))

    # doc = ""
    # for text in text_list:
    #     doc += " ".join(text.split())



    chunks = get_chunks_from_document(doc, size, overlap)

    return chunks
    
def get_chunks_from_document(doc: str, size: int=100, overlap:int= 10):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=size, chunk_overlap=overlap)
    texts = text_splitter.split_text(doc)

    return texts


def extract_text_from_pdf(file: str) -> List[str]:
    reader = PdfReader(file)
    text_list : List[str] = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_list.append(text)

    return text_list
