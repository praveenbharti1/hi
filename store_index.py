# # Initializing the Pinecone
from src.helper import load_pdf, text_split, download_huggingface_embedding
import pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_huggingface_embedding()

pinecone.Pinecone(api_key = PINECONE_API_KEY,
             environment = PINECONE_API_ENV)

index_name = "medical-chatbot"

docsearch = PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name = "medical-chatbot")