import streamlit as st
from langchain_core.messages import HumanMessage
from langgraph_backend import chatbot   # import compiled graph from backend

st.set_page_config(page_title="LangGraph Chatbot", page_icon="🤖")

st.title("🤖 LangGraph Chatbot (Groq + Streamlit)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Thread ID for LangGraph memory
thread_id = "streamlit-thread"

config = {"configurable": {"thread_id": thread_id}}

# Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input box
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Call LangGraph chatbot
    response = chatbot.invoke(
        {"messages": [HumanMessage(content=user_input)]},
        config=config
    )

    bot_reply = response["messages"][-1].content

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )