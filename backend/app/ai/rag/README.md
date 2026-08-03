# GrayProject RAG Module


## Overview

RAG module provides retrieval augmented generation capability.

It connects:

- Document ingestion
- Embedding system
- Vector storage
- Retrieval
- LLM generation


## Architecture


Question

↓

Retriever

↓

Context Builder

↓

LLM


## Modules


### ingestion

Document loading and preprocessing.


### retrieval

Search relevant knowledge.


### reranking

Optimize retrieved results.


### pipeline

Coordinate complete RAG workflow.


### schema

Common data structures.