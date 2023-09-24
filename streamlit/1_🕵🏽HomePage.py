# Importing the LLM features
import msticpy
from msticpy.context.contextproviders.llm import AgentRunner

import streamlit as st
import tempfile
from HtmlTemplate import bot_template, user_template, css

import nest_asyncio
nest_asyncio.apply()

# Suppress FutureWarning messages
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pygame.mixer


def main():
    """Main function of the App."""
    # Set up the page
    st.set_page_config(
        page_title="MSTICPy AI Assistant",
        page_icon="🤖",
        initial_sidebar_state="expanded",
        layout="centered"
    )

    st.write(css, unsafe_allow_html=True)
    
    st.markdown(
        """
        <style>
            .appview-container .main .block-container {{
                padding-top: 1rem;
                padding-bottom: 1rem;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image("msticpy2.png", use_column_width="auto")
    st.subheader("🤖 How can I assist your threat investigation today?")

    with st.sidebar:
        st.markdown(
            """
            <style>
                .css-1v7bkj4.ea3mdgi4 {
                    margin-top: -75px;
                }
            </style>
            """, 
            unsafe_allow_html=True
        )

        st.title("🤖 Welcome to MSTICPy AI")
        st.write("""
        Hello I'm the **MSTICpy AI-Powered Assistant**, crafted to navigate the world of threat intelligence with you. 
                    
        I am using LLMs coupled with MSTICpy to bolster your threat intelligence investigation.
        """)

        st.divider()
        st.subheader("🔑 OpenAI Configuration")
        st.write("First, configure your OpenAI API key and select the model you want to use. NB: if you are using a global variable for your API key you can skip this step.")
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")

        version = st.selectbox("Choose OpenAI Model version", ("3.5", "4.0"))
        MODEL = "gpt-3.5-turbo-16k" if version == "3.5" else "gpt-4"

        st.divider()
        #st.write("You can select the debug mode to see the process of the LLMs:")
        #debug_mode = st.sidebar.checkbox("Debug Mode")
        #stream_mode = st.sidebar.checkbox("Streaming Mode")
        st.subheader("⚙️ Select an Agent")
        st.write("""I am also configured to use multiple agents. 
                 Remember to configure the API keys for each agent you want to use in **msticpyconfig.yaml**.""")
        #vt_key = st.text_input("VirusTotal API Key", key="ti_key", type="password")
        selected_provider = st.radio(
            "Select Threat Intel Provider", 
            ["VirusTotal", "Alienvault OTX", "Risk IQ"], 
            key="provider", 
            horizontal=True
        )
        
        if selected_provider == "VirusTotal":
            agent = "VTAgent"
        elif selected_provider == "Alienvault OTX":
            agent = "OTXAgent"
        elif selected_provider == "Risk IQ":
            agent = "RiskIQAgent"

        st.write("Selected Provider:", selected_provider)
        st.write("Whenever you're ready, ask me what you want, and I'll investigate for you! 😉")

        st.divider()
        st.subheader("🥷 About the Team")
        st.markdown(
            """
            - Thomas Roccia
            - Ashwin Patil
            - Arjun Trivedi
            - Vignesh Nayak
            - Aditi Shah
            - Julien Touche
            - Wilman Rodriguez
            """
         )
        st.divider()
        st.write("Made with ♥ by the MSTICpy AI Team ")

        
    # Check if session state variables exist, if not initialize them
    if "user_msgs" not in st.session_state:
        st.session_state.user_msgs = []

    if "bot_msgs" not in st.session_state:
        st.session_state.bot_msgs = []

    if 'ready_to_download' not in st.session_state:
        st.session_state.ready_to_download = False
    
    # Initialize the sound
    pygame.mixer.init()
    sound = pygame.mixer.Sound('note.wav')

    with st.form("my_form", clear_on_submit=True):

        input_text = st.text_area(
            label="Enter your prompt:", 
        )

        submitted = st.form_submit_button("Run investigation")

        if submitted:
            agent_runner = AgentRunner()

            with st.spinner(input_text):
                result = AgentRunner.run_agent(agent, prompt=input_text, debug=True, openai_api_key=openai_api_key, model_name=MODEL)
                # Append user's message to the session state list
                st.session_state.user_msgs.append(input_text)
                # Append bot's response to the session state list
                st.session_state.bot_msgs.append(result)

            # Display the conversation history
            for user_msg, bot_msg in zip(st.session_state.user_msgs, st.session_state.bot_msgs):
                sound.play()
                st.write(user_template.replace("{{MSG}}", user_msg), unsafe_allow_html=True)
                st.write(bot_template.replace("{{MSG}}", bot_msg), unsafe_allow_html=True)
            
            # After updating conversation history
            st.session_state.ready_to_download = True
                
    # Outside of the form
    if st.session_state.ready_to_download:
        conversation_str = ""
        for user_msg, bot_msg in zip(st.session_state.user_msgs, st.session_state.bot_msgs):
            conversation_str += "Analyst: " + user_msg + "\n"
            conversation_str += "MSTICpy Assistant: " + bot_msg + "\n\n"

        tfile = tempfile.NamedTemporaryFile(delete=False) 
        path = tfile.name + ".txt"

        with open(path, 'w') as f:
            f.write(conversation_str)

        st.download_button(label="Download conversation history", data=conversation_str, file_name="conversation.txt", mime="text/plain")


if __name__ == "__main__":
    main()
