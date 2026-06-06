# Agentic Conversational AI Platform using LangGraph

## Overview

This project is a production-oriented conversational AI platform built using LangGraph, Retrieval-Augmented Generation (RAG), persistent memory, tool calling, and vector search. The system was designed to move beyond traditional chatbot implementations by introducing stateful workflows, long-term conversation persistence, document-aware question answering, and extensible agent capabilities.

The primary objective of the project was to explore how modern AI agents can maintain context across conversations, retrieve information from external knowledge sources, and intelligently decide when to invoke tools to improve response quality.

Unlike conventional chatbot architectures that rely solely on prompt engineering, this implementation leverages LangGraph's state management capabilities to create a more structured, scalable, and maintainable conversational system.


# Problem Statement

Most traditional chatbots suffer from several limitations:

* Conversations are often stateless.
* Context is lost between sessions.
* Responses are limited to model knowledge.
* No support for external tools.
* Difficulty handling long-running workflows.
* Limited ability to interact with custom knowledge bases.

These limitations make it difficult to build conversational systems suitable for real-world applications.

This project addresses those challenges by integrating:

* Persistent memory
* Retrieval-Augmented Generation (RAG)
* Tool calling
* Multi-thread conversation management
* Structured agent workflows

into a unified conversational AI platform.
# Key Objectives

* Build a stateful AI agent using LangGraph.
* Enable persistent conversation memory.
* Implement document-aware question answering using RAG.
* Support tool execution within conversations.
* Create scalable workflows using graph-based orchestration.
* Develop a user-friendly interface using Streamlit.



# System Architecture

```text
User
 │
 ▼
Streamlit Interface
 │
 ▼
LangGraph StateGraph
 │
 ├───────────────┐
 │               │
 ▼               ▼
LLM          Tool Node
 │               │
 ▼               ▼
Response     External Tools
 │
 ▼
Checkpointing Layer
 │
 ▼
SQLite Memory Store
 │
 ▼
Persistent Conversations

# Core Features

## 1. Stateful Agent Architecture

The system utilizes LangGraph's StateGraph framework to manage conversational state across multiple interactions.

Unlike traditional chains, LangGraph allows conversations to be represented as directed workflows where information flows between nodes and state can be preserved throughout the execution lifecycle.

Benefits include:

* Better workflow control
* Stateful execution
* Extensible architecture
* Easier debugging and maintenance

---

## 2. Persistent Memory

One of the most important capabilities of this project is conversation persistence.

The platform stores chat history using SQLite-based checkpointing.

### Technologies Used

* SqliteSaver
* AsyncSqliteSaver

### Benefits

* Conversations survive application restarts.
* Historical context can be recovered.
* Users can continue previous sessions.
* Enables long-term conversational experiences.

### Design Trade-off

SQLite provides simplicity and local persistence but may not scale efficiently for large distributed systems.

Future implementations could migrate to:

* PostgreSQL
* Redis
* Managed cloud databases

---

## 3. Multi-Thread Conversation Management

The system supports multiple independent conversation threads.

Each thread maintains its own context and memory.

Example:

```text
Thread A → Interview Preparation
Thread B → RAG Testing
Thread C → Technical Discussion
```

This architecture allows users to switch between conversations without losing context.

---

## 4. Retrieval-Augmented Generation (RAG)

To improve factual accuracy, the project incorporates a Retrieval-Augmented Generation pipeline.

### Workflow

```text
Document
   │
   ▼
PDF Loader
   │
   ▼
Text Chunking
   │
   ▼
Embedding Generation
   │
   ▼
FAISS Vector Database
   │
   ▼
Retriever
   │
   ▼
LLM
```

### Components

* PyPDFLoader
* RecursiveCharacterTextSplitter
* OpenAI Embeddings
* FAISS
* Retriever

### Benefits

* Reduced hallucinations
* Domain-specific knowledge
* Improved answer grounding
* Enhanced reliability

---

## 5. Tool Calling

The project supports external tool execution through LangGraph's ToolNode architecture.

### Example Tool

* DuckDuckGo Search

The agent can determine when external information is required and invoke tools dynamically.

Benefits:

* Access to current information
* Improved factual responses
* Extensible architecture

---

## 6. Streaming Responses

The application supports token streaming to provide real-time feedback to users.

Benefits:

* Better user experience
* Faster perceived response times
* Improved conversational flow

---

# Technology Stack

## Frontend

* Streamlit

## AI Frameworks

* LangChain
* LangGraph

## LLM Providers

* OpenAI
* Groq

## Vector Database

* FAISS

## Document Processing

* PyPDFLoader
* RecursiveCharacterTextSplitter

## Memory Layer

* SQLite
* SqliteSaver
* AsyncSqliteSaver

## Programming Language

* Python

---

# Why LangGraph?

LangGraph was selected instead of a simple LangChain chain because it provides:

* Stateful workflows
* Explicit graph execution
* Tool orchestration
* Memory management
* Better support for agentic systems

### Trade-off

The learning curve and implementation complexity are significantly higher.

However, the architecture becomes more scalable and production-friendly.

---

# Challenges Faced

## Managing Conversation State

Maintaining context across multiple threads required careful handling of state transitions and checkpointing.

## Memory Persistence

Ensuring reliable conversation recovery introduced additional architectural complexity.

## RAG Integration

Building an efficient retrieval pipeline required experimentation with chunk sizes and retrieval strategies.

## Tool Orchestration

Determining when the agent should invoke external tools required workflow design considerations.

---

# Future Enhancements

Several improvements are planned for future versions:

### Advanced Agent Workflows

* Multi-agent collaboration
* Specialized agents for different tasks

### Enhanced Memory

* Long-term memory systems
* User personalization

### Improved Retrieval

* Hybrid search
* Reranking models
* Metadata filtering

### Production Databases

Replace SQLite with:

* PostgreSQL
* Redis
* Cloud-native storage

### Additional Tools

* Calendar scheduling
* Email integration
* Weather APIs
* Knowledge graph querying

### Deployment

* Docker
* Kubernetes
* Cloud deployment pipelines

---

# Learning Outcomes

Through this project, I gained practical experience in:

* Agentic AI systems
* LangGraph workflows
* Retrieval-Augmented Generation
* Vector databases
* Tool calling
* Persistent memory systems
* Stateful conversational architectures
* Production-oriented AI application development

---

# Conclusion

This project demonstrates the development of an advanced conversational AI platform that combines memory, retrieval, tool usage, and graph-based orchestration into a unified system. By leveraging LangGraph and modern AI engineering practices, the platform moves beyond traditional chatbot implementations and provides a strong foundation for building scalable, production-ready AI assistants.
