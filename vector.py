from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_chroma import Chroma
import os 
import pandas as pd 

# loading the realistic restaurant reviews dataset and reading it using pandas
df = pd.read_csv("realistic_restaurant_reviews.csv")

# defining the embedding part here using OllamaEmbeddings 
# Each text chunk → convert into a vector (embedding)
embeddings = OllamaEmbeddings(model="mxbai-embed-large") 

# Check if vector DB folder already exists 
# (meaning: “we already have embeddings stored; don’t generate again”)
# If the folder DOES NOT exist → add_documents = True
# If the folder exists → add_documents = False
db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

# we are preparing here data into the documents
# Prepare documents only if DB does not exist
# Each CSV row becomes one Document containing the combined text, metadata, and a unique ID.
# So 100 rows → 100 documents, 100 IDs, 100 metadata entries, and 100 embeddings stored in the vector DB.
if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

# Creates (or loads) a persistent Chroma DB inside ./chrome_langchain_db
# If folder exists → it will load previous data
# If folder doesn’t exist → it creates a fresh DB
vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

# Add documents into Chroma (only first time)
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    

# here it will look for 5 releavnt reviews from the vector database
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
