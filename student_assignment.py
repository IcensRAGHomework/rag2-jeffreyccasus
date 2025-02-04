from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
  # load pdf
  loader = PyPDFLoader(q1_pdf)
  documents = loader.load()
  print("Pages in the original document: ", len(documents))

  # CharacterTextSplitter
  text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
  docs = text_splitter.split_documents(documents)
  page_count = len(docs)
  print("Length of chunks after splitting pages: ", len(docs))
  print("the last page", docs[page_count-1])

  return docs[page_count-1

def hw02_2(q2_pdf):
    pass
