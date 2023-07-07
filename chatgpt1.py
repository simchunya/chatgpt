import os
import sys
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import constants
import pathlib

def main():
    os.environ["OPENAI_API_KEY"] = constants.APIKEY
    query = sys.argv[1]
    #query = input("What is your query\n")
    print(query)

    #loader = TextLoader('data.txt')
    loader = DirectoryLoader(pathlib.Path("."), glob = "*.txt")
    index = VectorstoreIndexCreator().from_loaders([loader])
    reply = (index.query(query, llm = ChatOpenAI()))
    print(reply)
    #with open('readme.txt', 'w') as f:
        #f.write(f' this is the reply: {reply}')
    return

if __name__ == "__main__":
    main()