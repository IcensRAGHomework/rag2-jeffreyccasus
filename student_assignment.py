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
#from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import (CharacterTextSplitter, RecursiveCharacterTextSplitter)

def print_spit_docs(doc_array):
  for chunk in doc_array:
    #print(f"Chunk size: {len(chunk)}")
    print(chunk.page_content)
    print("\n")

def hw02_2(q2_pdf):
  # load pdf
  loader = PyPDFLoader(q2_pdf, mode = "single")
  documents = loader.load()
  print(documents)
  print("\n")

  # RecursiveCharacterTextSplitter
  recursive_text_splitter = RecursiveCharacterTextSplitter(
      chunk_size = 100,
      chunk_overlap  = 0,
      is_separator_regex = True,
      separators=["法規名稱：", "\n   第 ", "\n第 "],
  )

  split_texts = recursive_text_splitter.split_documents(documents)

  # debug
  #print_spit_docs(split_texts)

  print(f'\nlen of split_texts: {len(split_texts)}')
  return len(split_texts)
