# ARTICLE RESEARCH TOOL
This project is a web application that helps users research articles by providing a question-answering interface and displaying relevant sources.
The application utilizes the Langchain library to process and embed documents, and the OpenAI API to generate answers and identify relevant sources.

Usage
To use the application, follow these steps:

Clone the project repository.
Install the project dependencies using pip install -r requirements.txt.
Run the application using streamlit run app.py.
Enter the URLs of the articles you want to research in the "ARTICLE URLs" section of the sidebar.
Click the "Process URL" button.
Enter a question about the articles in the "Question" field.
Click the "Submit" button.
The application will process the articles and display the answer to your question, along with relevant sources.

Features
The application provides the following features:

Question-answering interface: Users can ask questions about the articles and receive relevant answers.
Source identification: The application identifies relevant sources for each answer.
Document embedding: The application embeds documents using the Langchain library to facilitate efficient retrieval.


Dependencies
The project depends on the following libraries:

streamlit
pickle
time
langchain
langchain.OpenAI
langchain.chains.RetrievalQAWithSourcesChain
langchain.chains.qa_with_sources.loading
langchain.text_splitter.RecursiveCharacterTextSplitter
langchain.document_loaders.UnstructuredURLLoader
langchain.embeddings.OpenAIEmbeddings
langchain.embeddings.HuggingFaceEmbeddings
langchain.vectorstores.FAISS
dotenv
Contributing
Contributions to the project are welcome. Please follow these guidelines:

Fork the project repository.
Create a new branch for your changes.
Make your changes to the code.
Add tests for your changes. 
Submit a pull request to the main branch.
License
The project is licensed under the MIT License.
