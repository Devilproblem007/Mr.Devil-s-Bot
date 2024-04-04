# Mr.Devil-s-Bot
import streamlit as st
import google.generativeai as genai


genai.configure(api_key="")
def ai(txt):
    
 for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(comment)    
return response.text




st.title("Mr.Devil's Ai Assistant")

command = st.chat_input("what is your need form m")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])


if command:
    with st.chat_message("USER"):
        st.write(command)
        st.session_state.message.append({"role":"USER","message":"command"})
    if "Hello" in command:
        with st.chat_message("BOT"):
            st.write("Hi How are you?")
            st.session_state.message.append({"role":"BOT","message":"Hi How are you?"})
    elif "Who are you" in command:
        with st.chat_message("BOT"):
            st.write("Im Mr.Devil's AI Assistant")
            st.session_state.message.append({"role":"BOT","message":"Im Mr.Devil's AI Assistant"})
    elif "Oii" in command:
        with st.chat_message("BOT"):
            st.write("Sollu Buddy")
            st.session_state.message.append({"role":"BOT","message":"Sollu buddy"}
    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})




