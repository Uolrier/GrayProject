# GrayProject

A modular personal AI system built from scratch.

GrayProject focuses on building a complete AI application infrastructure, including LLM orchestration, local inference runtime, prompt engineering, memory management, RAG knowledge systems, and an extensible AI workspace.

---

## Version

Current Version:

**v0.2.0-U**

This release completes the core LLM infrastructure and the first complete RAG knowledge system of GrayProject.

---

# Features

## LLM Core

* Unified LLM abstraction
* Multiple provider support
* OpenAI compatible API support
* DeepSeek integration
* Local HuggingFace inference runtime
* Model switching system
* Streaming response

## Generation

* Temperature control
* Top-p control
* Max token control
* Generation configuration management

## Conversation System

* Chat session management
* Conversation memory
* Context management
* Context truncation policy
* System prompt support

## Prompt Engineering

* Prompt templates
* Prompt builder
* Prompt debugging tools
* Prompt injection protection

## AI Infrastructure

* Embedding provider architecture
* Tokenizer abstraction
* Token usage tracking
* Modular provider and registry architecture

## RAG Knowledge System

* Multi-format document ingestion
* Text and Markdown support
* PDF and Word document support
* HTML and JSON support
* Python, Java, JavaScript and C++ source code support
* Git repository ingestion
* Configurable document chunking
* Semantic chunking
* Code-aware chunking
* Embedding pipeline
* Batch embedding
* Embedding cache
* Chroma vector database integration
* Knowledge base management
* Vector retrieval
* Multi-knowledge-base retrieval
* Hybrid retrieval architecture
* BGE reranking
* Cross-encoder reranking support
* Incremental indexing
* Document state tracking
* Index rebuild and update management
* Query caching
* RAG evaluation framework
* Retrieval accuracy evaluation

## Frontend

* Vue-based frontend
* Modular workspace architecture
* Chat interface
* Knowledge base integration
* Workspace state management
* Window management
* Configurable workspace themes

## Reliability

* Timeout handling
* Retry mechanism
* Rate limiting
* Error logging
* Security filtering
* Prompt injection protection

## Testing

* Unit tests
* Integration tests
* API tests
* RAG pipeline tests
* Retrieval accuracy evaluation
* Large-scale indexing tests
* Large-scale retrieval tests
* Incremental update tests
* Rebuild tests
* Performance benchmarks
* LLM stress testing

---

# Architecture

GrayProject is organized around several independent subsystems:

```text
                      GrayProject
                           │
        ┌──────────────────┼────────────────┐
        │                  │                │
       LLM                RAG           Frontend
        │                  │                │
   ┌────┴────┐        ┌────┴─────┐      Workspace
   │         │        │          │
Providers  Runtime  Ingestion  Retrieval
   │         │        │          │
OpenAI    HuggingFace │       Reranking
DeepSeek  Local       │          │
                      └────┬─────┘
                           │
                     Vector Store
                           │
                        Chroma
```

The system is designed around modular interfaces, registries, factories, managers, and independently testable components.

---

# Project Structure

```text
GrayProject

├── backend/
│   └── app/
│       ├── ai/
│       │   ├── embeddings/       Embedding providers
│       │   ├── prompts/          AI prompt system
│       │   └── rag/              RAG knowledge system
│       │
│       ├── llm/                  LLM abstraction and providers
│       ├── runtime/              Local inference runtime
│       ├── security/             Security and input filtering
│       ├── core/                 Infrastructure utilities
│       ├── api/                  API infrastructure
│       └── routers/               Application routes
│
├── frontend/
│   └── src/
│       ├── modules/              Feature modules
│       ├── shared/               Shared frontend components
│       ├── stores/               Application state
│       └── router/               Frontend routing
│
├── tests/
│   ├── unit/                     Unit tests
│   ├── integration/              Integration tests
│   ├── evaluation/               RAG evaluation
│   ├── performance/              Performance tests
│   └── api/                      API tests
│
├── config/                       Application configuration
├── docs/                         Architecture and development docs
├── scripts/                      Development and utility scripts
├── models/                       Local model directory
└── experiments/                  Experimental implementations
```

---

# RAG Pipeline

The current RAG system follows a modular processing pipeline:

```text
Documents
    │
    ▼
Document Loader
    │
    ▼
Document / Metadata
    │
    ▼
Chunking
    │
    ├── Fixed Length
    ├── Overlap
    ├── Semantic
    └── Code Aware
    │
    ▼
Embedding
    │
    ▼
Vector Store
    │
    ▼
Retrieval
    │
    ├── Vector Retrieval
    ├── Multi-KB Retrieval
    └── Hybrid Retrieval
    │
    ▼
Reranking
    │
    ├── BGE
    └── Cross Encoder
    │
    ▼
Context Construction
    │
    ▼
LLM
```

The architecture is designed to support future retrieval strategies and vector database implementations without coupling the entire pipeline to a single provider.

---

# Quick Start

## Backend

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
python backend/run.py
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available through the Vite development server.

---

# Development Status

## Completed

### Phase0

* Project initialization
* Development environment
* Engineering workflow
* Initial project infrastructure

### Phase1

* LLM Core architecture
* Provider abstraction
* Provider registry and factory
* Local inference runtime
* HuggingFace runtime integration
* Prompt system
* Conversation memory
* Context management
* Generation configuration
* Streaming response
* Security and prompt injection protection
* Reliability infrastructure

### Phase2

* RAG architecture
* Document abstraction
* Multi-format document ingestion
* Document chunking
* Semantic chunking
* Code-aware chunking
* Embedding pipeline
* Batch embedding
* Embedding cache
* Chroma vector database integration
* Knowledge base management
* Vector retrieval
* Multi-knowledge-base retrieval
* Hybrid retrieval architecture
* Reranking system
* BGE reranker
* Cross-encoder reranking support
* Incremental indexing
* Document state management
* Index update and rebuild
* Query cache
* RAG evaluation
* Retrieval accuracy testing
* Large-scale RAG performance testing
* Frontend workspace foundation

---

# Roadmap

Future development will focus on higher-level AI capabilities built on top of the existing LLM and RAG infrastructure.

Planned areas include:

* Agent framework
* Tool calling
* Task planning
* Long-term memory
* Personal AI assistant workflows
* More advanced knowledge management
* Expanded frontend workspace capabilities

---

# Documentation

Architecture and development documentation can be found under:

```text
docs/
```

Important documents include:

```text
docs/
├── architecture/
│   ├── llm_architecture.md
│   └── rag_architecture.md
│
├── development/
│   ├── setup.md
│   └── workflow.md
│
├── architecture.md
├── decisions.md
└── roadmap.md
```

---

# License

See [LICENSE](LICENSE) for license information.





# GrayProject

一个从零构建的模块化个人 AI 系统。

GrayProject 致力于构建完整的 AI 应用基础设施，包括：

* LLM 大语言模型调度系统
* 本地推理运行环境
* Prompt 工程系统
* 对话记忆管理
* RAG 知识库系统
* 可扩展 AI 应用架构

项目目标是构建一个具有工程化能力的个人 AI 助手基础平台。

---

# 版本信息

当前版本：

**v0.2.0-U**

该版本完成了 GrayProject 核心 AI 基础设施以及第一版完整 RAG 知识系统。

---

# 功能特性

## LLM 核心系统

* 统一的大语言模型抽象接口
* 多模型供应商支持
* OpenAI Compatible API 支持
* DeepSeek 接入
* HuggingFace 本地推理运行时
* 模型动态切换
* 流式输出响应

---

## 文本生成控制

支持：

* Temperature 参数控制
* Top-p 参数控制
* 最大 Token 数控制
* 统一生成配置管理

---

## 对话系统

包含：

* Chat 会话管理
* 多轮对话记忆
* 上下文管理
* 上下文截断策略
* System Prompt 支持

---

## Prompt 工程系统

包含：

* Prompt 模板管理
* Prompt Builder
* Prompt 调试工具
* Prompt 注入攻击防护

---

## AI 基础设施

包含：

* Embedding 模型抽象
* Tokenizer 抽象
* Token 使用统计
* Provider 注册机制
* Factory 工厂模式
* 模块化组件管理

---

# RAG 知识库系统

v0.2.0-U 完成了完整 RAG Pipeline：

## 文档处理

支持：

* TXT 文档
* Markdown 文档
* PDF 文档
* Word 文档
* HTML 页面
* JSON 数据
* Python 源码
* Java 源码
* JavaScript 源码
* C++ 源码
* Git 仓库解析

---

## 文档切分

支持：

* 固定长度切分
* 重叠窗口切分
* 语义切分
* 代码结构感知切分

---

## 向量化系统

包含：

* Embedding Pipeline
* 批量向量化
* Embedding 缓存
* 多 Embedding Provider 支持

---

## 向量数据库

目前支持：

* Chroma Vector Database

架构支持未来替换：

* FAISS
* 其他向量数据库

---

## 检索系统

支持：

* 向量相似度检索
* 多知识库检索
* Hybrid 混合检索架构

---

## 重排序系统

支持：

* BGE Reranker
* Cross Encoder Reranker

用于提升检索结果准确率。

---

## 知识库管理

包含：

* 多知识库管理
* 文档状态追踪
* 增量更新
* 索引更新
* 索引重建
* 查询缓存

---

## RAG 评估系统

包含：

* 检索准确率测试
* RAG Pipeline 测试
* 大规模数据测试
* 索引性能测试
* 增量更新测试

---

# 前端系统

当前前端基于 Vue 构建。

包含：

* 模块化前端架构
* AI Chat 页面
* Workspace 工作空间
* 知识库接口
* 状态管理
* 窗口管理
* 主题配置

---

# 系统可靠性

包含：

* 超时处理
* 请求重试
* 限流机制
* 错误日志
* 安全过滤
* Prompt Injection 防护

---

# 测试体系

项目包含完整测试体系：

## 单元测试

覆盖：

* LLM 模块
* RAG 模块
* Embedding 模块
* Tokenizer 模块
* Security 模块

---

## 集成测试

包含：

* API 测试
* Provider 测试
* 模型切换测试
* 完整 RAG Pipeline 测试

---

## 性能测试

包含：

* 大规模索引测试
* 大规模检索测试
* 增量更新测试
* 重建测试
* LLM 压力测试

---

# 项目结构

```text
GrayProject

├── backend
│   └── app
│       ├── llm
│       │   LLM模型抽象与供应商管理
│       │
│       ├── runtime
│       │   本地推理运行环境
│       │
│       ├── ai
│       │   ├── rag
│       │   │   RAG知识库系统
│       │   │
│       │   ├── embeddings
│       │   │   向量模型系统
│       │   │
│       │   └── prompts
│       │       Prompt系统
│       │
│       ├── security
│       │   安全模块
│       │
│       └── core
│           基础设施
│
├── frontend
│   Vue前端应用
│
├── tests
│   单元测试 / 集成测试 / 性能测试 / 评估测试
│
├── config
│   配置文件
│
├── docs
│   架构与开发文档
│
└── scripts
    开发辅助脚本
```

---

# RAG 数据流程

GrayProject 当前 RAG 流程：

```text
文件输入

    ↓

文档解析 Loader

    ↓

Document 数据结构

    ↓

文本切分 Chunk

    ↓

Embedding 向量化

    ↓

Vector Database

    ↓

Retriever 检索

    ↓

Reranker 重排序

    ↓

Context 构建

    ↓

LLM生成回答
```

---

# 快速开始

## 后端

创建 Python 环境：

```bash
python -m venv .venv
```

激活环境：

Linux:

```bash
source .venv/bin/activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

启动：

```bash
python backend/run.py
```

---

## 前端

进入前端目录：

```bash
cd frontend
```

安装依赖：

```bash
npm install
```

启动：

```bash
npm run dev
```

---

# 开发状态

## 已完成

## Phase0

完成：

* 项目初始化
* 开发环境搭建
* 工程化流程建立

---

## Phase1

完成：

* LLM Core 架构
* Provider 系统
* 本地推理 Runtime
* Prompt 系统
* Memory 系统
* Context 管理
* Streaming 输出
* 安全防护
* 可靠性基础设施

---

## Phase2

完成：

* RAG 系统架构设计
* 文档加载系统
* 多格式文档解析
* Chunk 切分系统
* Embedding Pipeline
* Chroma 向量数据库
* 知识库管理
* Retrieval 检索系统
* Hybrid Retrieval 架构
* Reranker 重排序
* 增量索引更新
* 文档状态管理
* RAG 评估系统
* 大规模性能测试
* 前端 Workspace 基础

---

# 后续规划

未来将在现有 LLM + RAG 基础上继续开发：

* Agent 系统
* Tool Calling
* 任务规划
* 长期记忆
* 个人 AI 助手工作流
* 更完善的知识管理
* 更丰富的前端工作空间

---

# 文档

详细架构和开发文档：

```text
docs/
```

包含：

* LLM 架构设计
* RAG 架构设计
* 开发流程
* 技术决策记录
* Roadmap

---

# License

详见：

```text
LICENSE
```
