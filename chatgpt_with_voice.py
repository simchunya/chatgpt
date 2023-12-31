import os
import sys
import speech_recognition
import pyttsx3
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import constants

def main():
    os.environ["OPENAI_API_KEY"] = constants.APIKEY
    query = listening_ear()
    reply = meaning_of_life(query)
    #query = input("What is your query\n")
    #print(query)
    speaker = pyttsx3.init()
    print(reply)
    speaker.say(reply)

def listening_ear():
    listener = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("robot: I'm listening")
        audio = listener.listen(mic)
        print("finished listening")
    try:
        query = listener.recognize_google(audio)
    except:
        query = "error i cant hear"
    print("You said: " + query)
    return(str(query))

def meaning_of_life(query):
    
    #loader = TextLoader('data.txt')
    loader = DirectoryLoader(".", glob = "*.txt")
    index = VectorstoreIndexCreator().from_loaders([loader])
    reply = (index.query(query, llm = ChatOpenAI()))
    
    return(reply)

if __name__ == "__main__":
    main()