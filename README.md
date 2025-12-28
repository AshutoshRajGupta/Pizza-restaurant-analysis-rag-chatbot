
# 🍕 Local RAG — Restaurant Review Analyzer

### Retrieve & Analyze Restaurant Reviews Using **Ollama + LangChain + ChromaDB**

This project is a **Local Retrieval-Augmented Generation (RAG) system** that answers questions about a restaurant based on **realistic customer reviews**.

It runs completely **offline**, powered by:

* 🧠 **Ollama LLMs**
* 🔗 **LangChain**
* 🗂 **ChromaDB**
* 📊 **CSV-based dataset**

Ask any question like:

> *"What do customers think about the pizza crust?"*
> *"What are the top complaints?"*
> *"Which pizzas are most praised?"*

The model answers using **actual retrieved reviews**.

---

## 📁 Project Structure

```
local-rag/
│── main.py                      # RAG pipeline & chatbot loop  
│── vector.py                    # Vector DB creation + retriever  
│── realistic_restaurant_reviews.csv   # Dataset  
│── requirements.txt             # Dependencies  
│── chrome_langchain_db/         # Auto-created vector DB  
│── venv/                        # Virtual environment  
```

---

## 🖼️ Screenshots

### 📌 **1. Dataset Preview (CSV File)**

<img width="1573" height="629" alt="image" src="https://github.com/user-attachments/assets/e567f5d6-b5f1-4e24-aac5-c4c855546bd9" />

---

### 📌 **2. Project Folder Structure (VS Code)**

<img width="1600" height="549" alt="image" src="https://github.com/user-attachments/assets/3d335d40-a0b6-42a9-9c09-4d44ff1e0eae" />

---

### 📌 **3. CLI RAG Chatbot Running**
<img width="1582" height="435" alt="image" src="https://github.com/user-attachments/assets/c6f38dc3-36d5-4fce-b9c9-4c72ccda4247" />
<img width="1586" height="201" alt="image" src="https://github.com/user-attachments/assets/2e21f761-9361-407f-8032-071454f84f29" />

---

## 🚀 Features

### 🔹 Local RAG Pipeline

Runs without cloud APIs using **Ollama**.

### 🔹 Smart Retrieval

Top 5 relevant reviews fetched using vector similarity.

### 🔹 Persistent Vector DB

Chroma saves embeddings & reloads instantly.

### 🔹 Uses Real Reviews

Answers directly grounded in CSV data.

### 🔹 Lightweight & Fast

Perfect for learning + portfolio projects.

---

## 🧠 How the RAG System Works

1. **Load CSV** (Pandas)
2. **Convert rows → LangChain Documents**
3. **Generate embeddings** using *mxbai-embed-large*
4. **Store vectors** in ChromaDB
5. **User asks a question**
6. **Retriever gets top 5 relevant reviews**
7. **Llama 3.2 generates the final answer**

---

## 🛠️ Installation

### 1️⃣ Install Ollama

[https://ollama.com/download](https://ollama.com/download)

Models required:

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

---

### 2️⃣ Setup Environment

```bash
uv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

---

### 3️⃣ Install Python Packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

You will see:

```
====================================
Ask your question (q to quit):
====================================
```

---

## 💬 Example Questions

* What do customers think about the service?
* Summarize the positive reviews.
* What complaints are mentioned most?
* Give feedback about thin crust pizza.
* Are there gluten-free options mentioned?

---

## 🧰 Tech Stack

| Component        | Purpose                |
| ---------------- | ---------------------- |
| 🐍 **Python**    | Application logic      |
| 🧠 **Ollama**    | Local LLM + embeddings |
| 🔗 **LangChain** | RAG chain              |
| 🗂 **ChromaDB**  | Vector storage         |
| 📊 **Pandas**    | CSV processing         |

---

## 📄 Dataset

Columns included:

* **Title**
* **Date**
* **Rating**
* **Review**

Used for retrieval + summarization.

---

## ⭐ Future Enhancements

* Streamlit UI version
* Sentiment Analysis
* Multi-query reasoning (Agentic RAG)
* Summary Dashboard

---

## ❤️ If this helped, give it a ⭐ on GitHub!

---

