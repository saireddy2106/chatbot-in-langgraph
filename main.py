
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


# llm = ChatGroq(
#     model="llama-3.3-70b-versatile",
#     api_key=""
# )


load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)



def chat_node(state: ChatState):

    messages = state['messages']

    response = llm.invoke(messages)

    return {'messages': [response]}

conn = sqlite3.connect(
    "chatbot.db",
    check_same_thread=False
)

checkpointer = SqliteSaver(conn)

graph = StateGraph(ChatState)

graph.add_node('chat_node',chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer = checkpointer)


def retrieve_all_threads():
    all_threads = set()

    for checkpoint in checkpointer.list(None):
        all_threads.add(
            checkpoint.config['configurable']['thread_id']
        )

    return list(all_threads)


# def retrieve_all_threads():
#     all_threads = set()
#     for checkpoint in checkpointer.list(None):
#         all_threads.add(checkpoint.config['configurable']['thread_id'])


#     return (list(all_threads))

# CONFIG = {
#     "configurable": {
#         "thread_id": "thread-1"
#     }
# }

# chatbot.invoke({'messages': [HumanMessage(content='hi my name is sai')]},
#             config= CONFIG)

# print(chatbot.get_state(config=CONFIG).values)
# stream=chatbot.stream(
#     {'messages': [HumanMessage(content='What is the process of making an ice cream?')]},
#     config= {
#         "configurable": {
#             "thread_id": "thread-1"
#         }
#     },
#     stream_mode='messages'
# )
# for message_chunk,metadata in stream:
#     if message_chunk.content:
#         print(message_chunk.content,end=" ",flush=True)




# for message_chunk, metadata in chatbot.stream(
#     {'messages' : [HumanMessage(content='What is the price of an ice cream?')]},
#     CONFIG = {
#         "configurable": {
#             "thread_id": "thread-1"
#         }
#     },
#     stream_mode='messages'
# ):
#     if message_chunk.content:
#         print(message_chunk.content,end=" ",flush=True)


# if __name__ == "__main__":
#     initial_state = {
        # 'messages': [HumanMessage(content='What is the capital of India')]
#     }

#     config = {
#         "configurable": {
#             "thread_id": "1"
#         }
#     }

#     chatbot.invoke(initial_state, config=config)['messages'][-1].content




#     while True:
#         user_message = input("Type here: ")

#         if user_message.strip().lower() in ['exit', 'quit', 'bye']:
#             break

#         response = chatbot.invoke(
#             {'messages': [HumanMessage(content=user_message)]},
#             config=config
#         )

#         print("AI:", response['messages'][-1].content)




# print("main.py loaded successfully")
# print("retrieve_all_threads:", retrieve_all_threads)
