
from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
import sqlite3

class ChatState(TypedDict):
  messages : Annotated[list[BaseMessage],add_messages]


load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)



def chat_node(state: ChatState):

    messages = state['messages']

    response = llm.invoke(messages)

    return {'messages': [response]}

conn = sqlite3.connect(database='chatbot.db',check_same_thread=False)

checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)

graph.add_node('chat_node',chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer = checkpointer)

CONFIG= {"configurable": {"thread_id": 'thread-1'}}

response = chatbot.invoke(
    {'messages': [HumanMessage(content='how do you fetch answers')]},
            config= CONFIG
)




print(response)
