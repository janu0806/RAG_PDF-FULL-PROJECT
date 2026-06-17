import streamlit as st
import tempfile
import os
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

from chunking import create_chunks
from vector_store import create_vector_store, retrieve_chunk
from local_llm import ask_local_llm
from pdf_reader import read_pdf

# Page Config
st.set_page_config(
    page_title="RAG AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: white;
}

.subtitle {
    text-align: center;
    color: #A0A0A0;
    font-size: 18px;
    margin-bottom: 30px;
}

.answer-box {
    padding: 25px;
    border-radius: 15px;
    background-color: #1A1D24;
    color: white;
    border: 1px solid #333;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);

}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    "<div class='title'>🤖 RAG PDF AI Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Upload any PDF and ask questions instantly using Local AI + FAISS</div>",
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.header("📂 Document Upload")
    uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

    st.markdown("---")

    st.markdown("""
### 🚀 Features

✅ PDF Question Answering

✅ FAISS Vector Search

✅ Local AI Model

✅ Semantic Retrieval

✅ Fast Responses
""")
    
    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# Main Section
question = st.text_input(
    "💬 Ask a Question",
    placeholder="Example: How many joints are used in the robot arm?"
)

col1, col2, col3 = st.columns([1,1,1])

with col2:
    submit = st.button("🔍 Get Answer", use_container_width=True)

# Processing

if submit:


    if not uploaded_files:
        st.warning("⚠️ Please upload at least one PDF.")

    elif question.strip() == "":
        st.warning("⚠️ Please enter a question.")

else:

    with st.spinner("🔍 Processing document..."):

        # Read all uploaded PDFs
        all_text = ""

        for uploaded_file in uploaded_files:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as tmp_file:

                uploaded_file.seek(0)
                tmp_file.write(uploaded_file.read())
                pdf_path = tmp_file.name

            text_from_pdf = read_pdf(pdf_path)
            all_text += "\n\n" + text_from_pdf

        # Backend Flow

            text = all_text
        st.write("Text Length:", len(text))

        chunks = create_chunks(text)

        st.write("Chunks Count:", len(chunks))

        index, embeddings = create_vector_store(chunks)

        context = retrieve_chunk(
            question,
            index,
            chunks
        )

        answer = ask_local_llm(
            context,
            question
        )

        st.session_state.chat_history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📄 Chunks", len(chunks))

        with col2:
            st.metric("🧠 Context Length", len(context))

        with col3:
            st.metric("⚡ Answer Length", len(answer))

    st.success("✅ Answer Generated")

    st.markdown("## 🤖 AI Response")

    st.markdown("### ❓ Question")
    st.info(question)

    st.markdown("### 🤖 Answer")
    st.success(answer)

    with st.expander("📄 Retrieved Context"):
        st.write(context)

# Chat History

st.markdown("## 💬 Chat History")

for chat in reversed(st.session_state.chat_history):

    st.markdown("### 👤 User")
    st.info(chat["question"])

    st.markdown("### 🤖 AI")
    st.success(chat["answer"])

    st.markdown("---")


# Footer

st.markdown("---")

st.markdown(
""" <center>
Made with ❤️ using Streamlit, FAISS and Local AI </center>
""",
unsafe_allow_html=True
)
