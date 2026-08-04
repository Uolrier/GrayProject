# GrayProject

A modular personal AI system built from scratch.

GrayProject focuses on building a complete AI application infrastructure, including LLM orchestration, local inference runtime, prompt engineering, memory management, and future RAG capabilities.

---

## Version

Current Version:


Official release of GrayProject LLM Core.

---

# Features

## LLM Core

- Unified LLM abstraction
- Multiple provider support
- OpenAI compatible API support
- DeepSeek integration
- Local HuggingFace inference runtime
- Model switching system
- Streaming response

## Generation

- Temperature control
- Top-p control
- Max token control
- Generation configuration management

## Conversation System

- Chat session management
- Conversation memory
- Context management
- Context truncation policy
- System prompt support

## Prompt Engineering

- Prompt templates
- Prompt builder
- Prompt debugging tools
- Prompt injection protection

## AI Infrastructure

- Embedding provider architecture
- Tokenizer abstraction
- Token usage tracking

## Reliability

- Timeout handling
- Retry mechanism
- Rate limiting
- Error logging

## Testing

- Unit tests
- Integration tests
- Provider tests
- Model switching tests
- Stress testing

---

# Project Structure
GrayProject

backend/
app/
llm/ LLM Core
runtime/ Local inference runtime
ai/ AI components
security/ Security modules
core/ Infrastructure

frontend/
Vue based frontend application

tests/
Unit, integration and performance tests

docs/
Architecture and development documents


---

# Quick Start

## Backend

Create environment:

```bash
python -m venv .venv

Activate:

Linux:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run backend:

python backend/run.py

Frontend

cd frontend

npm install

npm run dev

---

Development Status
Completed

Phase0:

Project initialization
Development environment
Engineering workflow

Phase1:

LLM Core architecture
Provider system
Runtime system
Prompt system
Memory system
Reliability infrastructure
Roadmap

Future phases:

RAG system
Vector database
Knowledge management
Agent framework
Local AI assistant