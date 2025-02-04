from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"

# HW1
def hw02_1(q1_pdf):
  # load pdf
  loader = PyPDFLoader(q1_pdf)
  documents = loader.load()
  print("Pages in the original document: ", len(documents))

  # CharacterTextSplitter
  text_splitter = CharacterTextSplitter(separator="\n\n", chunk_overlap=0)
  docs = text_splitter.split_documents(documents)
  page_count = len(docs)
  print("Length of chunks after splitting pages: ", len(docs))
  print("the last page", docs[page_count-1])

  return docs[page_count-1]

# HW2
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter, RecursiveCharacterTextSplitter)

def hw02_2(q2_pdf):
  # load pdf
  loader = PyPDFLoader(q2_pdf)
  documents = loader.load()
  print(documents)

  # RecursiveCharacterTextSplitter
  recursive_text_splitter = RecursiveCharacterTextSplitter(
      chunk_size = 500,
      chunk_overlap  = 0,
      separators=["法規名稱：", "修正日期：", "\n   第 ", "\n第 "],
  )

  recursive_splitted_texts = recursive_text_splitter.split_documents(documents)

  print(f'len of recursive_splitted_texts: {len(recursive_splitted_texts)}')

  return len(recursive_splitted_texts)
