# Mobile Packages Assistant

## Overview
The **Mobile Packages Assistant** is a Streamlit-based application that helps users find the best mobile packages based on their queries. It uses **LangChain**, **Groq's Llama3 model**, and **Hugging Face embeddings** to retrieve and generate relevant responses from a dataset of mobile packages.

## Features
- 💡 **Question-Answering System:** Ask about mobile packages and get relevant answers.
- 🤖 **AI-powered Retrieval:** Uses Groq's **Llama3-8B** model for responses.
- 🔍 **Semantic Search:** Uses Hugging Face embeddings to understand queries.
- ⚡ **Fast & Efficient:** In-memory vector store for quick retrieval.
- 📊 **User-Friendly Interface:** Built with Streamlit for an interactive experience.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/mobile-packages-assistant.git
   cd mobile-packages-assistant
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Add your **Groq API Key** in `secrets.toml` (for local testing) or in **Streamlit Cloud secrets**:
   ```toml
   GROQ_API_KEY = "your_actual_api_key"
   ```

## Running the App
Start the Streamlit app by running:
```sh
streamlit run app.py
```

## How It Works
1. Loads **mobile_packages.csv** dataset.
2. Splits the data into chunks for efficient retrieval.
3. Embeds the chunks using **Hugging Face embeddings**.
4. Stores embeddings in an **in-memory vector store**.
5. Retrieves relevant data based on the user's query.
6. Uses **Llama3-8B** to generate an answer.
7. Displays the answer in the Streamlit UI.

## Example Query
_"What is the best package for PUBG?"_

## DEPLOYMENT
This is deploy on a hugging face
https://huggingface.co/spaces/Aniq-63/Pakistan_Mobile_Packages/blob/main/app.py

## Dependencies
- Python 3.8+
- Streamlit
- LangChain
- Hugging Face Transformers
- Groq API

## License
MIT License

## Author
Aniq Ramzan

