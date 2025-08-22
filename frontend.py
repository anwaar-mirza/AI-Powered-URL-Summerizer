from backend import YouTubeSummarizer
from langchain_community.document_loaders import WebBaseLoader
from essentials import *
import streamlit as st
import validators

st.session_state.setdefault("bot", None)
st.session_state.setdefault("initialize", False)

st.set_page_config(
    page_title="🔴 AI-Powered URL Summarizer",
    layout="wide",
)


if not st.session_state.initialize:
    st.session_state.bot = YouTubeSummarizer(prompt=system_prompt)
    st.session_state.initialize = True

st.title("🔴 AI-Powered URL Summarizer")
st.header("Instant Summaries from YouTube Videos & Web Articles")
input_url = st.text_input("Enter YouTube Video URL or Web Article Link", placeholder="https://www.youtube.com/watch?v=example")
if input_url:
    if not validators.url(input_url):
        st.error("Please enter a valid URL.")
    else:
        with st.spinner("Generating summary..."):
            if "youtube.com" in input_url:
                video_id = extract_youtube_id(input_url)
                input_text = extract_transcript(video_id)
            else:
                headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
                input_text = WebBaseLoader(input_url, header_template=headers)
                input_text = input_text.load()
            
            results = st.session_state.bot.get_response(input_text)
            st.success("✅ Summary generated successfully!")
            st.write(results, unsafe_allow_html=True)
else:
    st.warning("⚠️ Please enter a URL to generate a summary.")
