
import streamlit as st
from main import chatbot
from langchain_core.messages import HumanMessage
import uuid



######function to generate thread ids
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_id():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversations(thread_id):
    return chatbot.get_state(config={"configurable": {"thread_id": thread_id}}).values.get('messages',[])

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

if 'thread_id' not in st.session_state:
    st.session_state['thread_id']=generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []
    add_thread(st.session_state['thread_id'])


#SIDEBAR UI
st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_id()

st.sidebar.button('My Conversations')

for thread_id in st.session_state['chat_threads'] [::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversations(thread_id)

        temp_messages = []

        for msg in messages:
            if isinstance(msg,HumanMessage):
                role = 'user'
            else:
                role = 'assistant'
            temp_messages.append({'role':role,'content':msg.content})
        st.session_state['message_history'] = temp_messages
####MAIN UI
#storing the message history in session state of streamlit
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


CONFIG = {
    "configurable": {
        "thread_id": st.session_state['thread_id']
    }
}

user_input = st.chat_input('Type Here')



if user_input:
    with st.chat_message('user'):
        st.text(user_input)

    # response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]},config=CONFIG)
    # ai_message = response['messages'][-1].content

    #st.session_state['message_history'].append({'role': 'assistant','content':ai_message})


    with st.chat_message('assistant'):
        ai_message=st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
            config= {
                "configurable": {
                    "thread_id": st.session_state['thread_id']
                }
            },
            stream_mode='messages'
            )
        )

    st.session_state['message_history'].append({'role': 'user','content':user_input})
    st.session_state['message_history'].append({'role': 'assistant','content':ai_message})

