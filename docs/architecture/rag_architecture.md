# GrayProject RAG Architecture


## 1. Overview

GrayProject RAG module provides retrieval augmented generation capability.

The purpose is to allow LLM to answer questions based on external knowledge sources,
including:

- local documents
- project files
- knowledge bases
- user provided data


## 2. High Level Architecture


User Question

    |
    v

RAG Pipeline

    |
    +----------------+
    |                |
    v                v

Retriever       LLM Generator

    |
    v

Vector Store

    |
    v

Embedding Model



## 3. Module Design


ai/rag

├── ingestion

Document importing and preprocessing


├── retrieval

Knowledge retrieval


├── reranking

Search result optimization


├── pipeline

RAG workflow orchestration


├── schema

Data structures


└── config

RAG configuration



## 4. Data Flow


Document

    |

Document Loader

    |

Text Splitter

    |

Embedding

    |

Vector Store


Query

    |

Query Embedding

    |

Vector Search

    |

Relevant Chunks

    |

Prompt Construction

    |

LLM Generation



## 5. Integration


### Embedding

RAG uses existing embedding abstraction:

ai.embeddings


Supported providers:

- BGE
- Jina
- OpenAI


### LLM

RAG uses existing LLM abstraction:

ai.llm


Supported providers:

- OpenAI
- DeepSeek
- OpenAI Compatible


### Prompt

RAG context will be injected through existing prompt system.


## 6. Design Principles


### Loose Coupling

RAG components communicate through abstract interfaces.


### Replaceable Components

Vector database, embedding model and retriever can be replaced independently.


### Unified Data Model

All documents are represented by common schema.


## 7. Future Extensions


Possible future support:

- hybrid search
- reranking models
- multi-vector retrieval
- knowledge graph
- agent based retrieval