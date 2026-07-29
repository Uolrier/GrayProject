# GrayProject LLM Architecture


## 1. Overview

LLM module is the core AI capability layer of GrayProject.

It provides unified interfaces for different language model providers.


## 2. Position in System

Frontend
    |
Backend API
    |
AI Service Layer
    |
LLM Module


## 3. Supported Providers

Future support:

- DeepSeek API
- OpenAI API
- Ollama
- Transformers Local Model


## 4. Design Principle

The upper layer should not depend on specific LLM providers.

All models should follow the same interface.


## 5. Module Structure

backend/app/ai/

├── llm

├── embeddings

├── prompts

└── agents


## 6. Future Extension

LLM module will support:

- RAG
- Agent
- Local inference
- Memory system