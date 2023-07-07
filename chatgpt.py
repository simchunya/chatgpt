import os
import sys
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import constants

def meaning_of_life(query):
    os.environ["OPENAI_API_KEY"] = constants.APIKEY

    #query = input("What is your query\n")
    #print(query)

    #loader = TextLoader('data.txt')
    loader = DirectoryLoader(".", glob = "*.txt")
    index = VectorstoreIndexCreator().from_loaders([loader])
    reply = (index.query(query, llm = ChatOpenAI()))
    print(reply)
    return(reply)