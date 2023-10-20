import os
import streamlit as st
import pickle
import time
import langchain
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import SeleniumURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()  #take environment variables from .env

st.title("ARTICLE RESEARCH TOOL 📈")
st.sidebar.title("ARTICLE URLs")

urls=[]
for i in range(3):
    url=st.sidebar.text_input(f"URL{i+1}")
    urls.append(url)

process_url_clicked=st.sidebar.button("Process URL")
file_path="faiss_store_openai.pkl"

main_placefolder=st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)




if process_url_clicked:
    #load_data
    loader = SeleniumURLLoader(urls=urls)
    main_placefolder.text("Data loading... started..✅✅✅")
    data=loader.load()
    #split_data
    text_spitter=RecursiveCharacterTextSplitter(
        separators=['\n\n','\n','.',','],
        chunk_size=1000
    )
    main_placefolder.text("Text splitting... started..✅✅✅")
    docs = text_spitter.split_documents(data)
    #create embeddings and save it to FAISS index
    embeddings = HuggingFaceEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs,embeddings)
    main_placefolder.text("Embedding vector Started Building..✅✅✅")
    time.sleep(2)

    #save the FAISS index to a pickle file
    with open(file_path,"wb") as f:
        pickle.dump(vectorstore_openai, f)

query = main_placefolder.text_input("Question: ")

if query:
    if os.path.exists(file_path):
        with open(file_path,"rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever = vectorstore.as_retriever())
            result = chain({"question":query}, return_only_outputs=True)
            st.header("Answer")
            st.write(result["answer"])

            #Display sources if available
            sources = result.get("sources","")
            if sources:
                st.subheader("Sources:")
                sources_list= sources.split("\n") #split the sources by newline
                for source in sources_list:
                    st.write(source)
            