# Project GrayProject


## Phase 0 —— 项目初始化（Project Foundation）

**目标：** 建立整个项目的工程基础，后续所有 Phase 都建立在此之上。

---

## Epic A：项目规划（Project Planning）

| Step          | 名称                   |
| ------------- | -------------------- |
| Phase0_Step01 | 明确项目目标（Vision）       |
| Phase0_Step02 | 确定整体技术栈（Tech Stack）  |
| Phase0_Step03 | 确定整体架构（Architecture） |
| Phase0_Step04 | 制定开发路线图（Roadmap）     |

---

## Epic B：项目仓库（Repository）

| Step          | 名称              |
| ------------- | --------------- |
| Phase0_Step05 | 创建 Git 仓库       |
| Phase0_Step06 | 建立 GitHub 仓库并关联 |
| Phase0_Step07 | 制定 Commit 规范    |
| Phase0_Step08 | 初始化 README      |

---

## Epic C：工程目录（Project Structure）

| Step          | 名称              |
| ------------- | --------------- |
| Phase0_Step09 | 创建根目录结构         |
| Phase0_Step10 | Backend 工程初始化   |
| Phase0_Step11 | Frontend 工程初始化  |
| Phase0_Step12 | Docs 文档目录初始化    |
| Phase0_Step13 | Scripts 工具目录初始化 |
| Phase0_Step14 | Tests 测试目录初始化   |

---

## Epic D：Python 开发环境（Development Environment）

| Step          | 名称                  |
| ------------- | ------------------- |
| Phase0_Step15 | 创建 Python 虚拟环境      |
| Phase0_Step16 | 安装基础依赖              |
| Phase0_Step17 | CUDA / PyTorch 环境验证 |
| Phase0_Step18 | requirements 管理     |

---

## Epic E：配置系统（Configuration）

| Step          | 名称             |
| ------------- | -------------- |
| Phase0_Step19 | 配置文件设计（config） |
| Phase0_Step20 | 环境变量管理（.env）   |
| Phase0_Step21 | 全局配置加载器        |

---

## Epic F：日志系统（Logging）

| Step          | 名称     |
| ------------- | ------ |
| Phase0_Step22 | 日志模块设计 |
| Phase0_Step23 | 控制台日志  |
| Phase0_Step24 | 文件日志   |
| Phase0_Step25 | 全局异常日志 |

---

## Epic G：Backend（FastAPI）

| Step          | 名称           |
| ------------- | ------------ |
| Phase0_Step26 | FastAPI 初始化  |
| Phase0_Step27 | 第一个 API      |
| Phase0_Step28 | Swagger 配置   |
| Phase0_Step29 | 全局异常处理       |
| Phase0_Step30 | Backend 启动验证 |

---

## Epic H：Frontend（Vue）

| Step          | 名称       |
| ------------- | -------- |
| Phase0_Step31 | Vue3 初始化 |
| Phase0_Step32 | 路由配置     |
| Phase0_Step33 | Axios 配置 |
| Phase0_Step34 | 首页搭建     |
| Phase0_Step35 | 前后端连通测试  |

---

## Epic I：开发规范（Engineering）

| Step          | 名称                   |
| ------------- | -------------------- |
| Phase0_Step36 | Black / Ruff 配置      |
| Phase0_Step37 | Pre-commit 配置        |
| Phase0_Step38 | License              |
| Phase0_Step39 | .gitignore 完善        |
| Phase0_Step40 | 项目首次 Release（v0.0.1） |

---

# 🎯 Phase0 Milestone（阶段验收）

完成以下内容后，**Phase 0 正式结束**：

* ✅ 项目目录完整
* ✅ Git 与 GitHub 正常使用
* ✅ Python 环境可复现
* ✅ FastAPI 正常运行
* ✅ Vue 正常运行
* ✅ 前后端可通信
* ✅ 配置系统完成
* ✅ 日志系统完成
* ✅ 工程规范建立
* ✅ 发布 **v0.0.1**

---

**PM 备注（路线调整）**

我对 Phase0 做了一个小调整：虽然我们目前已经讨论到了 **Phase0_Step03**，但后续我们仍以这份正式路线图作为唯一标准执行。如果在开发过程中发现某个 Step 需要进一步拆分（例如一个 Step 实际工作量过大），PM 会在不改变整体路线的前提下，把它拆成若干子任务（例如 `Phase0_Step27.1`、`Phase0_Step27.2`），而不会修改主编号。这样既能保持路线稳定，又能适应实际开发。


——————————————————————————————————————————————————————————————————————————————————————————


# GrayProject

# Phase 1 —— LLM Core（大语言模型核心）

**目标：** 建立统一的大模型调用层，使整个系统与具体模型解耦，为后续 RAG、Memory、Agent 提供统一入口。

---

# Epic A：LLM 架构设计

| Step          | 名称              |
| ------------- | --------------- |
| Phase1_Step01 | LLM 模块总体设计      |
| Phase1_Step02 | BaseLLM 抽象接口    |
| Phase1_Step03 | LLM 工厂（Factory） |
| Phase1_Step04 | Provider 注册机制   |

---

# Epic B：模型接入

| Step          | 名称                          |
| ------------- | --------------------------- |
| Phase1_Step05 | OpenAI 接入                   |
| Phase1_Step06 | DeepSeek API 接入             |
| Phase1_Step07 | OpenAI Compatible 接口统一      |
| Phase1_Step08 | Local Inference Runtime 抽象|
| Phase1_Step09 | HuggingFace Transformers 接入 |
| Phase1_Step10 | 模型切换机制                      |

---

# Epic C：聊天接口

| Step          | 名称               |
| ------------- | ---------------- |
| Phase1_Step11 | ChatRequest 定义   |
| Phase1_Step12 | ChatResponse 定义  |
| Phase1_Step13 | Chat Session 管理  |
| Phase1_Step14 | System Prompt 支持 |
| Phase1_Step15 | 多轮上下文管理          |

---

# Epic D：Prompt Engine

| Step          | 名称                  |
| ------------- | ------------------- |
| Phase1_Step16 | Prompt Template     |
| Phase1_Step17 | Prompt Builder      |
| Phase1_Step18 | Prompt Injection 防护 |
| Phase1_Step19 | Prompt Debug 工具     |

---

# Epic E：Embedding

| Step          | 名称               |
| ------------- | ---------------- |
| Phase1_Step20 | BaseEmbedding 接口 |
| Phase1_Step21 | OpenAI Embedding |
| Phase1_Step22 | BGE Embedding    |
| Phase1_Step23 | Jina Embedding   |
| Phase1_Step24 | Embedding 统一管理   |

---

# Epic F：Token 管理

| Step          | 名称           |
| ------------- | ------------ |
| Phase1_Step25 | Tokenizer 接口 |
| Phase1_Step26 | Token 统计     |
| Phase1_Step27 | 上下文长度控制      |
| Phase1_Step28 | 自动截断策略       |

---

# Epic G：Streaming

| Step          | 名称     |
| ------------- | ------ |
| Phase1_Step29 | 流式输出接口 |
| Phase1_Step30 | SSE 支持 |
| Phase1_Step31 | 前端流式显示 |
| Phase1_Step32 | 中断生成   |

---

# Epic H：模型配置

| Step          | 名称             |
| ------------- | -------------- |
| Phase1_Step33 | Temperature 配置 |
| Phase1_Step34 | Top-p 配置       |
| Phase1_Step35 | Max Tokens 配置  |
| Phase1_Step36 | Provider 配置中心  |

---

# Epic I：异常处理

| Step          | 名称       |
| ------------- | -------- |
| Phase1_Step37 | API 异常处理 |
| Phase1_Step38 | 超时重试     |
| Phase1_Step39 | 限流处理     |
| Phase1_Step40 | 错误日志记录   |

---

# Epic J：阶段验收

| Step          | 名称            |
| ------------- | ------------- |
| Phase1_Step41 | 模型切换测试        |
| Phase1_Step42 | 多 Provider 联调 |
| Phase1_Step43 | 压力测试          |
| Phase1_Step44 | 发布 v0.1.0     |

---

# 🎯 Phase1 Milestone（阶段验收）

完成以下内容后，**Phase 1 正式结束**：

* ✅ 已实现统一 LLM 接口
* ✅ 支持多个模型 Provider（API + 本地）
* ✅ 支持多轮对话
* ✅ 支持 Streaming
* ✅ Prompt Engine 可复用
* ✅ Embedding 接口完成
* ✅ Token 管理完成
* ✅ 异常处理完善
* ✅ 发布 **v0.1.0**

---

## PM 备注

这一阶段**不涉及 Agent、RAG、Memory**。

Phase 1 的职责只有一个：

> **把所有模型能力封装成统一接口。**

后续所有模块（RAG、Memory、Tool、Agent）都只能调用 `BaseLLM` 和 `BaseEmbedding`，而不能直接依赖某个具体模型。这是整个系统后续可扩展性的基础。


——————————————————————————————————————————————————————————————————————————————————————————


# GrayProject

# Phase 2 —— RAG（Retrieval-Augmented Generation）

**目标：** 构建完整的知识库系统，让 AI 能够理解和检索本地文件，为 Memory、Agent 提供知识基础。

---

# Epic A：RAG 架构设计

| Step          | 名称                |
| ------------- | ----------------- |
| Phase2_Step01 | RAG 总体架构设计        |
| Phase2_Step02 | Document 抽象接口     |
| Phase2_Step03 | Loader 工厂设计       |
| Phase2_Step04 | Index Pipeline 设计 |

---

# Epic B：文档加载（Document Loader）

| Step          | 名称                |
| ------------- | ----------------- |
| Phase2_Step05 | TXT Loader        |
| Phase2_Step06 | Markdown Loader   |
| Phase2_Step07 | PDF Loader        |
| Phase2_Step08 | Word Loader       |
| Phase2_Step09 | Excel Loader      | (跳过)
| Phase2_Step10 | PowerPoint Loader |（跳过）
| Phase2_Step11 | HTML Loader       |
| Phase2_Step12 | JSON Loader       |

---

# Epic C：代码知识库

| Step          | 名称                             |
| ------------- | ------------------------------ |
| Phase2_Step13 | Python Loader                  |
| Phase2_Step14 | C/C++ Loader                   |
| Phase2_Step15 | Java Loader                    |
| Phase2_Step16 | JavaScript / TypeScript Loader |
| Phase2_Step17 | Git 仓库导入                       |
| Phase2_Step18 | README 解析                      |

---

# Epic D：Chunk（文本切分）

| Step          | 名称            |
| ------------- | ------------- |
| Phase2_Step19 | 固定长度切分        |
| Phase2_Step20 | Overlap 切分    |
| Phase2_Step21 | Markdown 结构切分 |
| Phase2_Step22 | Code Chunk    |
| Phase2_Step23 | 语义切分          |
| Phase2_Step24 | Chunk 参数配置    |

---

# Epic E：Embedding Pipeline

| Step          | 名称              |
| ------------- | --------------- |
| Phase2_Step25 | 文档向量化           |
| Phase2_Step26 | 批量 Embedding    |
| Phase2_Step27 | Embedding Cache |
| Phase2_Step28 | 增量更新            |

---

# Epic F：向量数据库

| Step          | 名称            |
| ------------- | ------------- |
| Phase2_Step29 | Chroma 接入     |
| Phase2_Step30 | Collection 管理 |
| Phase2_Step31 | Metadata 管理   |
| Phase2_Step32 | Index 更新      |
| Phase2_Step33 | 删除与重建         |

---

# Epic G：Retriever

| Step          | 名称                |
| ------------- | ----------------- |
| Phase2_Step34 | Top-K 检索          |
| Phase2_Step35 | Similarity Search |
| Phase2_Step36 | Metadata Filter   |
| Phase2_Step37 | 多知识库检索            |
| Phase2_Step38 | Hybrid Search（预留） |

---

# Epic H：Reranker

| Step          | 名称            |
| ------------- | ------------- |
| Phase2_Step39 | Reranker 接口   |
| Phase2_Step40 | BGE Reranker  |
| Phase2_Step41 | Cross Encoder |
| Phase2_Step42 | 检索排序优化        |

---

# Epic I：知识库管理

| Step          | 名称     |
| ------------- | ------ |
| Phase2_Step43 | 创建知识库  |
| Phase2_Step44 | 删除知识库  |
| Phase2_Step45 | 导入目录   |
| Phase2_Step46 | 自动扫描更新 |
| Phase2_Step47 | 文档状态管理 |

---

# Epic J：查询流程

| Step          | 名称             |
| ------------- | -------------- |
| Phase2_Step48 | Query Pipeline |
| Phase2_Step49 | Context 拼接     |
| Phase2_Step50 | Security Pipeline V1（Prompt Injection Defense）|
| Phase2_Step51 | RAG Chat API   |
| Phase2_Step52 | 引用来源展示         |

---

# Epic K：优化

| Step          | 名称           |
| ------------- | ------------ |
| Phase2_Step53 | 查询缓存         |
| Phase2_Step54 | Embedding 缓存 |
| Phase2_Step55 | 大文件处理        |
| Phase2_Step56 | 并行索引构建       |

---

# Epic L：阶段验收

| Step          | 名称        |
| ------------- | --------- |
| Phase2_Step57 | 多格式文档联调   |
| Phase2_Step58 | 大规模知识库测试  |
| Phase2_Step59 | 检索准确率验证   |
| Phase2_Step60 | 发布 v0.2.0 |

---

# 🎯 Phase2 Milestone（阶段验收）

完成以下内容后，**Phase 2 正式结束**：

* ✅ 支持多种文档格式导入
* ✅ 支持代码仓库作为知识库
* ✅ 支持自动 Chunk 与 Embedding
* ✅ 支持向量数据库管理
* ✅ 支持 Top-K 检索
* ✅ 支持 Reranker 重排序
* ✅ 支持知识库管理与增量更新
* ✅ 支持 RAG 问答并展示引用来源
* ✅ 发布 **v0.2.0**

---

## PM 备注

Phase 2 的目标不是“聊天”，而是**建立 AI 的知识获取能力**。

完成这一阶段后，AI 将能够读取和检索你的本地资料（文档、代码、笔记等），但**还不会形成长期记忆，也不会自主决策**。这些能力将在后续的 Memory 和 Agent 阶段加入。


——————————————————————————————————————————————————————————————————————————————————————————


# GrayProject

# Phase 3 —— Memory（记忆系统）

**目标：** 构建 AI 的短期记忆、长期记忆和用户画像系统，使 AI 能够真正“记住”过去，而不是每次都从零开始。

---

# Epic A：Memory 架构设计

| Step          | 名称              |
| ------------- | --------------- |
| Phase3_Step01 | Memory 总体架构设计   |
| Phase3_Step02 | BaseMemory 抽象接口 |
| Phase3_Step03 | Memory Manager  |
| Phase3_Step04 | Memory 生命周期设计   |

---

# Epic B：短期记忆（Short-Term Memory）

| Step          | 名称                  |
| ------------- | ------------------- |
| Phase3_Step05 | Conversation Buffer |
| Phase3_Step06 | Token Window 管理     |
| Phase3_Step07 | 上下文裁剪策略             |
| Phase3_Step08 | Session 管理          |
| Phase3_Step09 | 多会话隔离               |

---

# Epic C：长期记忆（Long-Term Memory）

| Step          | 名称               |
| ------------- | ---------------- |
| Phase3_Step10 | 长期记忆结构设计         |
| Phase3_Step11 | Memory 存储模型      |
| Phase3_Step12 | Memory Embedding |
| Phase3_Step13 | Memory 向量化       |
| Phase3_Step14 | 长期记忆数据库          |

---

# Epic D：记忆提取（Memory Extraction）

| Step          | 名称          |
| ------------- | ----------- |
| Phase3_Step15 | 对话信息提取      |
| Phase3_Step16 | 用户信息识别      |
| Phase3_Step17 | 事件信息识别      |
| Phase3_Step18 | 偏好信息识别      |
| Phase3_Step19 | 目标信息识别      |
| Phase3_Step20 | 自动生成 Memory |

---

# Epic E：记忆检索（Memory Recall）

| Step          | 名称                |
| ------------- | ----------------- |
| Phase3_Step21 | Similarity Recall |
| Phase3_Step22 | 时间排序              |
| Phase3_Step23 | 权重排序              |
| Phase3_Step24 | 多条件检索             |
| Phase3_Step25 | Recall Pipeline   |

---

# Epic F：记忆更新（Memory Update）

| Step          | 名称        |
| ------------- | --------- |
| Phase3_Step26 | 新增 Memory |
| Phase3_Step27 | Memory 修改 |
| Phase3_Step28 | Memory 合并 |
| Phase3_Step29 | Memory 删除 |
| Phase3_Step30 | 冲突处理      |

---

# Epic G：Memory Summary

| Step          | 名称                   |
| ------------- | -------------------- |
| Phase3_Step31 | Conversation Summary |
| Phase3_Step32 | Daily Summary        |
| Phase3_Step33 | Weekly Summary       |
| Phase3_Step34 | Knowledge Summary    |
| Phase3_Step35 | 自动摘要更新               |

---

# Epic H：用户画像（User Profile）

| Step          | 名称           |
| ------------- | ------------ |
| Phase3_Step36 | Profile 数据结构 |
| Phase3_Step37 | 兴趣建模         |
| Phase3_Step38 | 技能建模         |
| Phase3_Step39 | 长期目标建模       |
| Phase3_Step40 | Profile 自动更新 |

---

# Epic I：遗忘机制（Memory Forgetting）

| Step          | 名称           |
| ------------- | ------------ |
| Phase3_Step41 | Memory 重要性评分 |
| Phase3_Step42 | 时间衰减机制       |
| Phase3_Step43 | 自动清理策略       |
| Phase3_Step44 | 用户手动管理       |
| Phase3_Step45 | Memory 压缩    |

---

# Epic J：Memory API

| Step          | 名称           |
| ------------- | ------------ |
| Phase3_Step46 | Memory 查询接口  |
| Phase3_Step47 | Memory 写入接口  |
| Phase3_Step48 | Memory 编辑接口  |
| Phase3_Step49 | Memory 可视化接口 |
| Phase3_Step50 | Memory 调试工具  |

---

# Epic K：安全与隐私

| Step          | 名称          |
| ------------- | ----------- |
| Phase3_Step51 | Memory 权限设计 |
| Phase3_Step52 | 敏感信息过滤      |
| Phase3_Step53 | 加密存储        |
| Phase3_Step54 | 数据导出        |
| Phase3_Step55 | 数据备份与恢复     |

---

# Epic L：阶段验收

| Step          | 名称          |
| ------------- | ----------- |
| Phase3_Step56 | 多轮记忆联调      |
| Phase3_Step57 | 长短期记忆协同测试   |
| Phase3_Step58 | 用户画像验证      |
| Phase3_Step59 | Memory 性能测试 |
| Phase3_Step60 | 发布 v0.3.0   |

---

# 🎯 Phase3 Milestone（阶段验收）

完成以下内容后，**Phase 3 正式结束**：

* ✅ 支持短期记忆（上下文管理）
* ✅ 支持长期记忆（向量化存储）
* ✅ 自动从对话提取重要信息
* ✅ 支持记忆检索、更新、删除
* ✅ 支持用户画像自动构建
* ✅ 支持摘要与记忆压缩
* ✅ 支持遗忘机制与隐私保护
* ✅ Memory API 完整可调用
* ✅ 发布 **v0.3.0**

---

## PM 备注

这是整个 GrayProject 的**第一个质变阶段**。

从这一阶段开始，AI 不再只是“读取知识库”，而是开始形成**持续成长的个人记忆系统**。

同时，我建议从这一阶段开始，将 Memory 划分为三类：

1. **System Memory**：系统运行所需信息（配置、状态、任务等）。
2. **Knowledge Memory**：来自 RAG 的知识和文档内容。
3. **Personal Memory**：用户相关的长期信息（偏好、项目、目标、历史决策等）。

后续的 Tool Calling、Agent 和 Automation 都将统一通过 Memory Manager 访问这三类记忆，而不是各自维护独立的数据。这样整个系统会保持一致性，也更容易扩展。


——————————————————————————————————————————————————————————————————————————————————————————


# GrayProject

# Phase 4 —— Tool Calling（工具调用系统）

**目标：** 赋予 AI 操作电脑和外部资源的能力，使其从“会回答问题”升级为“会执行任务”。

---

# Epic A：Tool 架构设计

| Step          | 名称                    |
| ------------- | --------------------- |
| Phase4_Step01 | Tool 总体架构设计           |
| Phase4_Step02 | BaseTool 抽象接口         |
| Phase4_Step03 | Tool Registry（工具注册中心） |
| Phase4_Step04 | Tool Manager（工具管理器）   |
| Phase4_Step05 | Tool 生命周期管理           |

---

# Epic B：Function Calling

| Step          | 名称                  |
| ------------- | ------------------- |
| Phase4_Step06 | Tool Schema 定义      |
| Phase4_Step07 | Function Calling 接口 |
| Phase4_Step08 | 参数解析器               |
| Phase4_Step09 | 参数校验                |
| Phase4_Step10 | Tool 调用流程           |

---

# Epic C：文件系统工具（File System）

| Step          | 名称      |
| ------------- | ------- |
| Phase4_Step11 | 文件读取    |
| Phase4_Step12 | 文件写入    |
| Phase4_Step13 | 文件复制与移动 |
| Phase4_Step14 | 文件删除    |
| Phase4_Step15 | 文件搜索    |
| Phase4_Step16 | 文件信息查询  |
| Phase4_Step17 | 目录遍历    |

---

# Epic D：Python Tool

| Step          | 名称             |
| ------------- | -------------- |
| Phase4_Step18 | Python Tool 接口 |
| Phase4_Step19 | 沙箱环境           |
| Phase4_Step20 | Python 脚本执行    |
| Phase4_Step21 | 返回结果解析         |
| Phase4_Step22 | 异常处理           |

---

# Epic E：Shell / CMD Tool

| Step          | 名称                  |
| ------------- | ------------------- |
| Phase4_Step23 | Shell Tool          |
| Phase4_Step24 | CMD/PowerShell Tool |
| Phase4_Step25 | 白名单机制               |
| Phase4_Step26 | 命令输出解析              |
| Phase4_Step27 | 危险命令拦截              |

---

# Epic F：Git Tool

| Step          | 名称         |
| ------------- | ---------- |
| Phase4_Step28 | Git 状态查询   |
| Phase4_Step29 | Git Commit |
| Phase4_Step30 | Git Branch |
| Phase4_Step31 | Git Pull   |
| Phase4_Step32 | Git Push   |
| Phase4_Step33 | Git Log    |

---

# Epic G：浏览器工具（Browser）

| Step          | 名称           |
| ------------- | ------------ |
| Phase4_Step34 | Browser Tool |
| Phase4_Step35 | 打开网页         |
| Phase4_Step36 | 页面抓取         |
| Phase4_Step37 | 下载文件         |
| Phase4_Step38 | 网页内容解析       |

---

# Epic H：办公工具（Office）

| Step          | 名称              |
| ------------- | --------------- |
| Phase4_Step39 | Excel Tool      |
| Phase4_Step40 | Word Tool       |
| Phase4_Step41 | PowerPoint Tool |
| Phase4_Step42 | PDF Tool        |
| Phase4_Step43 | CSV Tool        |

---

# Epic I：系统工具（System）

| Step          | 名称           |
| ------------- | ------------ |
| Phase4_Step44 | 系统信息获取       |
| Phase4_Step45 | CPU / GPU 信息 |
| Phase4_Step46 | 磁盘管理         |
| Phase4_Step47 | 网络状态         |
| Phase4_Step48 | 进程管理         |
| Phase4_Step49 | 应用启动         |

---

# Epic J：工具权限管理

| Step          | 名称              |
| ------------- | --------------- |
| Phase4_Step50 | Tool Permission |
| Phase4_Step51 | 用户确认机制          |
| Phase4_Step52 | 高危操作审批          |
| Phase4_Step53 | Tool 日志         |
| Phase4_Step54 | Tool 审计         |

---

# Epic K：Tool Pipeline

| Step          | 名称           |
| ------------- | ------------ |
| Phase4_Step55 | 单工具调用        |
| Phase4_Step56 | 多工具串联        |
| Phase4_Step57 | Tool Context |
| Phase4_Step58 | Tool Retry   |
| Phase4_Step59 | Tool Debug   |

---

# Epic L：阶段验收

| Step          | 名称        |
| ------------- | --------- |
| Phase4_Step60 | 工具联调测试    |
| Phase4_Step61 | 权限测试      |
| Phase4_Step62 | 多工具协同测试   |
| Phase4_Step63 | 性能测试      |
| Phase4_Step64 | 发布 v0.4.0 |

---

# 🎯 Phase4 Milestone（阶段验收）

完成以下内容后，**Phase 4 正式结束**：

* ✅ 建立统一 Tool Framework
* ✅ 支持 Function Calling
* ✅ 支持文件系统操作
* ✅ 支持 Python、Shell、Git 工具
* ✅ 支持浏览器与 Office 工具
* ✅ 支持系统信息获取与应用启动
* ✅ 建立完整权限管理与安全机制
* ✅ 支持多工具串联执行
* ✅ 发布 **v0.4.0**

---

## PM 备注

这是 **GrayProject 的第二个质变阶段**。

从这一阶段开始，AI 将具备真正的**执行能力（Action）**，而不仅是回答问题。

同时，我建议在这一阶段确立一个长期原则：

> **所有工具都必须通过统一的 Tool Framework 接入，任何新工具（如 Docker、数据库、邮件、日历、MCP Server 等）都只能作为新的 Tool Plugin，而不能直接耦合到 Agent 或业务逻辑中。**

这样，后续 Phase 5 的 Agent 只需要负责**决策**，而 Tool Framework 负责**执行**，两者职责清晰，整个系统也更容易维护和扩展。


——————————————————————————————————————————————————————————————————————————————————————————


# GrayProject

# Phase 5 —— Agent（智能体系统）

**目标：** 构建 AI 的决策中枢，使其能够自主规划任务、调用工具、利用记忆和知识完成复杂目标，而不仅仅执行单一步骤。

---

# Epic A：Agent 架构设计

| Step          | 名称             |
| ------------- | -------------- |
| Phase5_Step01 | Agent 总体架构设计   |
| Phase5_Step02 | BaseAgent 抽象接口 |
| Phase5_Step03 | Agent Manager  |
| Phase5_Step04 | Agent 生命周期管理   |
| Phase5_Step05 | Agent 配置系统     |

---

# Epic B：任务理解（Task Understanding）

| Step          | 名称      |
| ------------- | ------- |
| Phase5_Step06 | 用户意图识别  |
| Phase5_Step07 | 任务分类    |
| Phase5_Step08 | 参数提取    |
| Phase5_Step09 | 目标标准化   |
| Phase5_Step10 | 任务复杂度评估 |

---

# Epic C：任务规划（Planning）

| Step          | 名称         |
| ------------- | ---------- |
| Phase5_Step11 | Planner 架构 |
| Phase5_Step12 | Task 分解    |
| Phase5_Step13 | 子任务生成      |
| Phase5_Step14 | 执行顺序规划     |
| Phase5_Step15 | 依赖关系分析     |
| Phase5_Step16 | 执行计划生成     |

---

# Epic D：执行器（Executor）

| Step          | 名称          |
| ------------- | ----------- |
| Phase5_Step17 | Executor 架构 |
| Phase5_Step18 | Tool 调度     |
| Phase5_Step19 | RAG 调度      |
| Phase5_Step20 | Memory 调度   |
| Phase5_Step21 | LLM 调度      |
| Phase5_Step22 | 执行结果收集      |

---

# Epic E：推理与反思（Reasoning）

| Step          | 名称             |
| ------------- | -------------- |
| Phase5_Step23 | ReAct 思想实现     |
| Phase5_Step24 | Observation 管理 |
| Phase5_Step25 | Reflection（反思） |
| Phase5_Step26 | Self Check（自检） |
| Phase5_Step27 | 决策修正           |

---

# Epic F：错误恢复（Recovery）

| Step          | 名称            |
| ------------- | ------------- |
| Phase5_Step28 | Tool Retry    |
| Phase5_Step29 | Planner Retry |
| Phase5_Step30 | 自动重新规划        |
| Phase5_Step31 | 回滚机制          |
| Phase5_Step32 | 失败原因分析        |

---

# Epic G：多 Agent（Multi-Agent）

| Step          | 名称             |
| ------------- | -------------- |
| Phase5_Step33 | Multi-Agent 架构 |
| Phase5_Step34 | Agent 通信       |
| Phase5_Step35 | Agent 协作       |
| Phase5_Step36 | Agent 角色管理     |
| Phase5_Step37 | Task 分配        |

---

# Epic H：上下文管理（Context）

| Step          | 名称              |
| ------------- | --------------- |
| Phase5_Step38 | Context Builder |
| Phase5_Step39 | Memory 注入       |
| Phase5_Step40 | RAG 注入          |
| Phase5_Step41 | Tool Result 注入  |
| Phase5_Step42 | Prompt Assembly |

---

# Epic I：任务管理（Task Manager）

| Step          | 名称            |
| ------------- | ------------- |
| Phase5_Step43 | Task Queue    |
| Phase5_Step44 | Task Status   |
| Phase5_Step45 | Task Priority |
| Phase5_Step46 | Task History  |
| Phase5_Step47 | Task Resume   |

---

# Epic J：Agent API

| Step          | 名称                |
| ------------- | ----------------- |
| Phase5_Step48 | Agent Chat API    |
| Phase5_Step49 | Agent Execute API |
| Phase5_Step50 | Agent Status API  |
| Phase5_Step51 | Agent Debug API   |
| Phase5_Step52 | Agent Monitor     |

---

# Epic K：性能优化

| Step          | 名称          |
| ------------- | ----------- |
| Phase5_Step53 | Planner 优化  |
| Phase5_Step54 | Tool 并行调用   |
| Phase5_Step55 | Context 压缩  |
| Phase5_Step56 | Agent Cache |
| Phase5_Step57 | 执行效率优化      |

---

# Epic L：阶段验收

| Step          | 名称           |
| ------------- | ------------ |
| Phase5_Step58 | 单 Agent 综合测试 |
| Phase5_Step59 | 多 Agent 协同测试 |
| Phase5_Step60 | 长任务稳定性测试     |
| Phase5_Step61 | 性能与资源测试      |
| Phase5_Step62 | 发布 v0.5.0    |

---

# 🎯 Phase5 Milestone（阶段验收）

完成以下内容后，**Phase 5 正式结束**：

* ✅ Agent 能理解复杂用户目标
* ✅ 能自动拆分并规划任务
* ✅ 能调度 LLM、Memory、RAG 和 Tool
* ✅ 支持 ReAct 推理流程
* ✅ 支持失败恢复与自动重规划
* ✅ 支持多 Agent 协作
* ✅ 建立完整 Task Manager
* ✅ 提供 Agent API 与监控能力
* ✅ 发布 **v0.5.0**

---

## PM 备注（重要调整）

这是我认为整个 **GrayProject 最核心的阶段**，也是第三次质变。

不过，结合目前 Agent 技术的发展趋势，我建议在真正开发 Phase 5 时做一个调整：

**不要把 Agent 写死成某一种论文或框架（例如只实现 ReAct）。** 应该设计成可插拔架构，例如：

* Planner（规划器）
* Executor（执行器）
* Memory Provider（记忆提供者）
* RAG Provider（知识提供者）
* Tool Provider（工具提供者）
* Reasoning Strategy（推理策略，如 ReAct、Plan-and-Execute、Reflexion 等）

这样未来即使接入新的 Agent 思路（例如 MCP、A2A、Graph Agent 或其他规划算法），也只需要替换某个模块，而不用重写整个系统。

**Phase 5 的目标不是做出“最聪明”的 Agent，而是搭建一个能够持续演进的 Agent 平台。**


—————————————————————————————————————————————————————————————————————————————————————————


# GrayProject

# Phase 6 —— Automation（自动化系统）

**目标：** 让 AI 从“接收指令执行任务”升级为“主动管理电脑和日常工作”，具备定时、事件驱动、工作流和后台运行能力。

---

# Epic A：Automation 架构设计

| Step          | 名称                  |
| ------------- | ------------------- |
| Phase6_Step01 | Automation 总体架构设计   |
| Phase6_Step02 | BaseAutomation 抽象接口 |
| Phase6_Step03 | Automation Manager  |
| Phase6_Step04 | Automation 生命周期管理   |
| Phase6_Step05 | Workflow 基础框架       |

---

# Epic B：任务调度（Scheduler）

| Step          | 名称            |
| ------------- | ------------- |
| Phase6_Step06 | Scheduler 架构  |
| Phase6_Step07 | 一次性任务         |
| Phase6_Step08 | 定时任务（Cron）    |
| Phase6_Step09 | 周期任务          |
| Phase6_Step10 | 延迟任务          |
| Phase6_Step11 | Scheduler 持久化 |

---

# Epic C：事件监听（Event）

| Step          | 名称         |
| ------------- | ---------- |
| Phase6_Step12 | Event 总线设计 |
| Phase6_Step13 | 文件变化监听     |
| Phase6_Step14 | 文件夹监听      |
| Phase6_Step15 | 系统启动事件     |
| Phase6_Step16 | 网络状态事件     |
| Phase6_Step17 | 自定义事件      |

---

# Epic D：Workflow（工作流）

| Step          | 名称               |
| ------------- | ---------------- |
| Phase6_Step18 | Workflow Builder |
| Phase6_Step19 | 条件判断节点           |
| Phase6_Step20 | Tool 节点          |
| Phase6_Step21 | Agent 节点         |
| Phase6_Step22 | Memory 节点        |
| Phase6_Step23 | Workflow 执行器     |
| Phase6_Step24 | Workflow 调试      |

---

# Epic E：后台服务（Background Service）

| Step          | 名称     |
| ------------- | ------ |
| Phase6_Step25 | 后台运行模式 |
| Phase6_Step26 | 服务状态管理 |
| Phase6_Step27 | 日志监控   |
| Phase6_Step28 | 自动恢复   |
| Phase6_Step29 | 资源占用优化 |

---

# Epic F：通知系统（Notification）

| Step          | 名称                   |
| ------------- | -------------------- |
| Phase6_Step30 | Notification Manager |
| Phase6_Step31 | 桌面通知                 |
| Phase6_Step32 | 系统托盘消息               |
| Phase6_Step33 | 消息中心                 |
| Phase6_Step34 | 通知优先级                |

---

# Epic G：自动化模板（Automation Templates）

| Step          | 名称             |
| ------------- | -------------- |
| Phase6_Step35 | 文件自动整理         |
| Phase6_Step36 | Downloads 自动分类 |
| Phase6_Step37 | Git 仓库自动检查     |
| Phase6_Step38 | 日志自动清理         |
| Phase6_Step39 | 定时知识库更新        |
| Phase6_Step40 | 自动生成日报         |

---

# Epic H：任务历史（History）

| Step          | 名称                 |
| ------------- | ------------------ |
| Phase6_Step41 | Automation History |
| Phase6_Step42 | 执行记录               |
| Phase6_Step43 | 错误记录               |
| Phase6_Step44 | 执行统计               |
| Phase6_Step45 | 历史查询               |

---

# Epic I：安全机制（Safety）

| Step          | 名称              |
| ------------- | --------------- |
| Phase6_Step46 | Automation 权限控制 |
| Phase6_Step47 | 高危任务确认          |
| Phase6_Step48 | 自动暂停机制          |
| Phase6_Step49 | 回滚机制            |
| Phase6_Step50 | Automation 审计日志 |

---

# Epic J：Automation API

| Step          | 名称            |
| ------------- | ------------- |
| Phase6_Step51 | 创建自动化任务 API   |
| Phase6_Step52 | 编辑自动化任务 API   |
| Phase6_Step53 | 删除自动化任务 API   |
| Phase6_Step54 | Workflow API  |
| Phase6_Step55 | Scheduler API |

---

# Epic K：性能优化

| Step          | 名称             |
| ------------- | -------------- |
| Phase6_Step56 | 多任务并发优化        |
| Phase6_Step57 | Workflow 缓存    |
| Phase6_Step58 | Scheduler 性能优化 |
| Phase6_Step59 | 后台资源优化         |

---

# Epic L：阶段验收

| Step          | 名称            |
| ------------- | ------------- |
| Phase6_Step60 | 自动化综合测试       |
| Phase6_Step61 | 长时间稳定性测试      |
| Phase6_Step62 | 多 Workflow 联调 |
| Phase6_Step63 | 性能与安全测试       |
| Phase6_Step64 | 发布 v0.6.0     |

---

# 🎯 Phase6 Milestone（阶段验收）

完成以下内容后，**Phase 6 正式结束**：

* ✅ 建立统一 Automation Framework
* ✅ 支持定时任务与周期任务
* ✅ 支持事件驱动自动化
* ✅ 支持可视化 Workflow 执行
* ✅ 支持后台持续运行
* ✅ 支持通知系统
* ✅ 提供常用自动化模板
* ✅ 支持任务历史、日志和统计
* ✅ 建立完整安全机制
* ✅ 发布 **v0.6.0**

---

## PM 备注（架构升级建议）

我建议将 **Automation** 定位为整个系统的**事件驱动层（Event-Driven Layer）**，而不是简单的“定时任务”。

也就是说，任何事件——例如文件变化、Git 仓库更新、知识库新增文档、用户登录、Agent 完成任务——都可以触发一个 Workflow。

形成统一的数据流：

```text
Event
   ↓
Automation Engine
   ↓
Workflow
   ↓
Agent / Tool / Memory / RAG
   ↓
Notification / Log
```

这样，Phase 6 不仅能完成“每天整理 Downloads”这样的自动化任务，还会成为未来语音助手、移动端同步、多设备协同等功能的基础设施，而无需重新设计整个系统。


—————————————————————————————————————————————————————————————————————————————————————————


# GrayProject

# Phase 7 —— Vision（视觉系统）

**目标：** 赋予 AI 理解屏幕、图片、文档和视频内容的能力，实现真正的多模态交互。

---

# Epic A：Vision 架构设计

| Step          | 名称                 |
| ------------- | ------------------ |
| Phase7_Step01 | Vision 总体架构设计      |
| Phase7_Step02 | BaseVision 抽象接口    |
| Phase7_Step03 | Vision Manager     |
| Phase7_Step04 | 多模态数据流设计           |
| Phase7_Step05 | Vision Provider 管理 |

---

# Epic B：图片理解（Image Understanding）

| Step          | 名称                  |
| ------------- | ------------------- |
| Phase7_Step06 | 图片加载                |
| Phase7_Step07 | 图片预处理               |
| Phase7_Step08 | 图片描述（Image Caption） |
| Phase7_Step09 | 图片问答（VQA）           |
| Phase7_Step10 | 多图片上下文理解            |

---

# Epic C：OCR（文字识别）

| Step          | 名称      |
| ------------- | ------- |
| Phase7_Step11 | OCR 接口  |
| Phase7_Step12 | 图片文字识别  |
| Phase7_Step13 | PDF OCR |
| Phase7_Step14 | 表格 OCR  |
| Phase7_Step15 | OCR 后处理 |

---

# Epic D：屏幕理解（Screen Understanding）

| Step          | 名称      |
| ------------- | ------- |
| Phase7_Step16 | 屏幕截图    |
| Phase7_Step17 | UI 元素识别 |
| Phase7_Step18 | 屏幕区域定位  |
| Phase7_Step19 | 屏幕内容理解  |
| Phase7_Step20 | 屏幕状态分析  |

---

# Epic E：视觉定位（Vision Grounding）

| Step          | 名称                 |
| ------------- | ------------------ |
| Phase7_Step21 | 目标检测               |
| Phase7_Step22 | 区域定位               |
| Phase7_Step23 | Bounding Box 管理    |
| Phase7_Step24 | 指向目标能力             |
| Phase7_Step25 | Grounding Pipeline |

---

# Epic F：视频理解（Video）

| Step          | 名称     |
| ------------- | ------ |
| Phase7_Step26 | 视频读取   |
| Phase7_Step27 | 关键帧提取  |
| Phase7_Step28 | 视频摘要   |
| Phase7_Step29 | 视频问答   |
| Phase7_Step30 | 视频事件识别 |

---

# Epic G：视觉知识库

| Step          | 名称           |
| ------------- | ------------ |
| Phase7_Step31 | 图片向量化        |
| Phase7_Step32 | 图片 Embedding |
| Phase7_Step33 | 图片检索         |
| Phase7_Step34 | 多模态 RAG      |
| Phase7_Step35 | 图片知识库管理      |

---

# Epic H：视觉工具（Vision Tool）

| Step          | 名称         |
| ------------- | ---------- |
| Phase7_Step36 | 截图工具       |
| Phase7_Step37 | 图片编辑工具     |
| Phase7_Step38 | OCR Tool   |
| Phase7_Step39 | 图像分析 Tool  |
| Phase7_Step40 | Vision API |

---

# Epic I：视觉 Agent

| Step          | 名称               |
| ------------- | ---------------- |
| Phase7_Step41 | Vision Agent     |
| Phase7_Step42 | 屏幕观察能力           |
| Phase7_Step43 | GUI 操作规划         |
| Phase7_Step44 | Vision + Tool 协同 |
| Phase7_Step45 | 多模态推理            |

---

# Epic J：性能优化

| Step          | 名称       |
| ------------- | -------- |
| Phase7_Step46 | 图片缓存     |
| Phase7_Step47 | GPU 推理优化 |
| Phase7_Step48 | 批量处理     |
| Phase7_Step49 | 多模态上下文优化 |

---

# Epic K：安全机制

| Step          | 名称        |
| ------------- | --------- |
| Phase7_Step50 | 隐私区域过滤    |
| Phase7_Step51 | 敏感信息识别    |
| Phase7_Step52 | 权限控制      |
| Phase7_Step53 | Vision 日志 |
| Phase7_Step54 | 数据管理      |

---

# Epic L：阶段验收

| Step          | 名称         |
| ------------- | ---------- |
| Phase7_Step55 | 图片理解测试     |
| Phase7_Step56 | OCR 综合测试   |
| Phase7_Step57 | 屏幕理解联调     |
| Phase7_Step58 | 多模态 RAG 测试 |
| Phase7_Step59 | 性能与稳定性测试   |
| Phase7_Step60 | 发布 v0.7.0  |

---

# 🎯 Phase7 Milestone（阶段验收）

完成以下内容后，**Phase 7 正式结束**：

* ✅ 建立统一 Vision Framework
* ✅ 支持图片理解与问答
* ✅ 支持 OCR（图片、PDF、表格）
* ✅ 支持屏幕理解与 UI 分析
* ✅ 支持目标检测与视觉定位
* ✅ 支持视频理解
* ✅ 支持多模态 RAG
* ✅ Vision 与 Agent、Tool 协同工作
* ✅ 建立视觉安全与隐私机制
* ✅ 发布 **v0.7.0**

---

## PM 备注（架构升级建议）

我建议将 **Vision** 不仅看作“图像识别”，而是整个系统的**多模态感知层（Perception Layer）**。

整体数据流建议设计为：

```text
Image / Screen / Video
          ↓
 Vision Framework
          ↓
 Perception Engine
          ↓
 Memory / RAG / Agent
          ↓
 Tool Calling
          ↓
 Action
```

也就是说，Vision 不负责“决策”，它只负责**感知世界**。真正的决策仍然由 Phase 5 的 Agent 完成，而 Vision 提供高质量的视觉信息输入。

这种分层设计会使未来接入新的视觉模型（如 OCR、VLM、GUI Agent 等）时，只需要扩展 Vision Framework，而不需要修改 Agent 或 Tool 层，从而保持整个 GrayProject 的架构稳定、易于演进。


—————————————————————————————————————————————————————————————————————————————————————————


# GrayProject

# Phase 8 —— Model（模型研发系统）

**目标：** 从"调用模型"进化到"理解模型、训练模型、优化模型"，最终拥有属于 GrayProject 自己的模型体系。

> **说明：** 这是整个项目最难、耗时最长的一个 Phase，也是你之前一直希望深入学习的方向（Transformer、nanoGPT、DeepSeek 等）最终汇聚的地方。

---

# Epic A：Transformer 基础

| Step          | 名称                       |
| ------------- | ------------------------ |
| Phase8_Step01 | Transformer 架构回顾         |
| Phase8_Step02 | Attention 原理实现           |
| Phase8_Step03 | Multi-Head Attention     |
| Phase8_Step04 | MLP / FFN 实现             |
| Phase8_Step05 | Positional Encoding      |
| Phase8_Step06 | LayerNorm 与 Residual     |
| Phase8_Step07 | Decoder Only Transformer |

---

# Epic B：Tokenizer

| Step          | 名称            |
| ------------- | ------------- |
| Phase8_Step08 | Tokenizer 原理  |
| Phase8_Step09 | BPE 实现        |
| Phase8_Step10 | SentencePiece |
| Phase8_Step11 | Tokenizer 训练  |
| Phase8_Step12 | Vocabulary 管理 |

---

# Epic C：MiniGPT（从零实现）

| Step          | 名称                      |
| ------------- | ----------------------- |
| Phase8_Step13 | 数据集准备                   |
| Phase8_Step14 | DataLoader              |
| Phase8_Step15 | 模型实现                    |
| Phase8_Step16 | Loss Function           |
| Phase8_Step17 | Optimizer               |
| Phase8_Step18 | Learning Rate Scheduler |
| Phase8_Step19 | Training Loop           |
| Phase8_Step20 | 推理（Inference）           |

---

# Epic D：训练系统

| Step          | 名称                    |
| ------------- | --------------------- |
| Phase8_Step21 | Checkpoint 管理         |
| Phase8_Step22 | Resume Training       |
| Phase8_Step23 | Mixed Precision       |
| Phase8_Step24 | Gradient Accumulation |
| Phase8_Step25 | Gradient Clipping     |
| Phase8_Step26 | TensorBoard / 日志      |
| Phase8_Step27 | 训练监控                  |

---

# Epic E：模型优化

| Step          | 名称                 |
| ------------- | ------------------ |
| Phase8_Step28 | Flash Attention 接入 |
| Phase8_Step29 | KV Cache           |
| Phase8_Step30 | RoPE               |
| Phase8_Step31 | SwiGLU             |
| Phase8_Step32 | RMSNorm            |
| Phase8_Step33 | 推理性能优化             |

---

# Epic F：现代 LLM 技术

| Step          | 名称                       |
| ------------- | ------------------------ |
| Phase8_Step34 | LoRA                     |
| Phase8_Step35 | QLoRA                    |
| Phase8_Step36 | PEFT 框架                  |
| Phase8_Step37 | Quantization（INT8 / FP8） |
| Phase8_Step38 | MoE 原理                   |
| Phase8_Step39 | MoE 简化实现                 |

---

# Epic G：源码阅读与复现

| Step          | 名称               |
| ------------- | ---------------- |
| Phase8_Step40 | nanoGPT 阅读总结     |
| Phase8_Step41 | minGPT 阅读总结      |
| Phase8_Step42 | DeepSeek-V3 阅读总结 |
| Phase8_Step43 | Llama 架构分析       |
| Phase8_Step44 | Qwen 架构分析        |
| Phase8_Step45 | Phi 系列架构分析       |

---

# Epic H：Atlas Model

| Step          | 名称               |
| ------------- | ---------------- |
| Phase8_Step46 | Atlas Model 架构设计 |
| Phase8_Step47 | Atlas Tokenizer  |
| Phase8_Step48 | Atlas 配置系统       |
| Phase8_Step49 | Atlas 训练框架       |
| Phase8_Step50 | Atlas 推理框架       |
| Phase8_Step51 | Atlas 模型评估       |

---

# Epic I：模型部署

| Step          | 名称               |
| ------------- | ---------------- |
| Phase8_Step52 | GGUF 导出          |
| Phase8_Step53 | ONNX 导出          |
| Phase8_Step54 | HuggingFace 格式支持 |
| Phase8_Step55 | 本地推理部署           |
| Phase8_Step56 | API 部署           |

---

# Epic J：性能评估

| Step          | 名称        |
| ------------- | --------- |
| Phase8_Step57 | Benchmark |
| Phase8_Step58 | 推理速度测试    |
| Phase8_Step59 | GPU 显存分析  |
| Phase8_Step60 | 模型质量评估    |

---

# Epic K：模型迭代

| Step          | 名称         |
| ------------- | ---------- |
| Phase8_Step61 | 小模型优化      |
| Phase8_Step62 | 指令微调       |
| Phase8_Step63 | RAG 联合测试   |
| Phase8_Step64 | Agent 联合测试 |
| Phase8_Step65 | 持续训练策略     |

---

# Epic L：阶段验收

| Step          | 名称               |
| ------------- | ---------------- |
| Phase8_Step66 | Atlas Model 综合测试 |
| Phase8_Step67 | 长时间推理稳定性测试       |
| Phase8_Step68 | 性能优化验收           |
| Phase8_Step69 | 模型文档整理           |
| Phase8_Step70 | 发布 v0.8.0        |

---

# 🎯 Phase8 Milestone（阶段验收）

完成以下内容后，**Phase 8 正式结束**：

* ✅ 深入理解 Transformer 全部核心模块
* ✅ 独立训练 MiniGPT
* ✅ 建立完整训练框架
* ✅ 掌握现代 LLM 优化技术（RoPE、RMSNorm、FlashAttention、LoRA、QLoRA 等）
* ✅ 完成多个开源模型源码阅读与总结
* ✅ 拥有 Atlas 自己的模型架构
* ✅ 支持训练、推理、部署完整流程
* ✅ 与 RAG、Memory、Tool、Agent 无缝集成
* ✅ 发布 **v0.8.0**

---

## PM 备注（重大调整）

这是我唯一建议**保持长期演进**的 Phase。

与你最初的想法相比，我做了一个重要调整：

> **Phase 8 的目标不是"造一个比 DeepSeek 更强的大模型"，而是"建立属于 GrayProject 的模型研发平台"。**

这样，未来每当你学习一个新模型，都可以把成果吸收到 GrayProject 中：

* 阅读 **nanoGPT** → 优化训练框架。
* 阅读 **DeepSeek-V3** → 引入新的 Attention、MoE 或推理优化。
* 阅读 **Llama / Qwen / Phi** → 借鉴成熟架构设计。
* 学习新的论文 → 作为新的模块或优化策略加入。

因此，**GrayProject** 将不是一个固定模型，而是一个持续迭代的模型家族。

这也与你最初的目标完全一致：利用自己的 GPU，在个人电脑上不断学习、实现、训练和演进，而不是一次性完成一个模型后停止。


—————————————————————————————————————————————————————————————————————————————————————————


# GrayProject

# Phase 9 —— Release（发布与产品化）

**目标：** 将 GrayProject 从一个开发项目，打磨成一个真正可以长期使用、展示、部署和持续迭代的个人 AI 产品。

---

# Epic A：Release 架构设计

| Step          | 名称                         |
| ------------- | -------------------------- |
| Phase9_Step01 | Release 总体规划               |
| Phase9_Step02 | 发布流程设计                     |
| Phase9_Step03 | 版本号规范（Semantic Versioning） |
| Phase9_Step04 | Changelog 管理               |

---

# Epic B：项目文档

| Step          | 名称                |
| ------------- | ----------------- |
| Phase9_Step05 | README 完善         |
| Phase9_Step06 | 快速开始（Quick Start） |
| Phase9_Step07 | 架构设计文档            |
| Phase9_Step08 | API 文档            |
| Phase9_Step09 | 开发者文档             |
| Phase9_Step10 | 常见问题（FAQ）         |

---

# Epic C：部署系统

| Step          | 名称             |
| ------------- | -------------- |
| Phase9_Step11 | Docker 部署      |
| Phase9_Step12 | Docker Compose |
| Phase9_Step13 | 环境变量配置         |
| Phase9_Step14 | 一键安装脚本         |
| Phase9_Step15 | 自动更新机制         |

---

# Epic D：工程质量

| Step          | 名称     |
| ------------- | ------ |
| Phase9_Step16 | 单元测试完善 |
| Phase9_Step17 | 集成测试   |
| Phase9_Step18 | 回归测试   |
| Phase9_Step19 | 性能测试   |
| Phase9_Step20 | 安全测试   |

---

# Epic E：CI/CD

| Step          | 名称               |
| ------------- | ---------------- |
| Phase9_Step21 | GitHub Actions   |
| Phase9_Step22 | 自动测试             |
| Phase9_Step23 | 自动构建             |
| Phase9_Step24 | 自动发布             |
| Phase9_Step25 | Release Artifact |

---

# Epic F：产品体验

| Step          | 名称     |
| ------------- | ------ |
| Phase9_Step26 | UI 优化  |
| Phase9_Step27 | UX 优化  |
| Phase9_Step28 | 设置页面   |
| Phase9_Step29 | 用户引导   |
| Phase9_Step30 | 错误反馈系统 |

---

# Epic G：数据管理

| Step          | 名称          |
| ------------- | ----------- |
| Phase9_Step31 | 数据备份        |
| Phase9_Step32 | 数据恢复        |
| Phase9_Step33 | 配置导入导出      |
| Phase9_Step34 | Memory 导入导出 |
| Phase9_Step35 | 知识库迁移       |

---

# Epic H：作品集建设

| Step          | 名称          |
| ------------- | ----------- |
| Phase9_Step36 | GitHub 仓库整理 |
| Phase9_Step37 | 项目 Wiki     |
| Phase9_Step38 | 技术博客整理      |
| Phase9_Step39 | 项目演示视频      |
| Phase9_Step40 | 项目展示网站      |

---

# Epic I：版本发布

| Step          | 名称                    |
| ------------- | --------------------- |
| Phase9_Step41 | Alpha 发布              |
| Phase9_Step42 | Beta 发布               |
| Phase9_Step43 | RC（Release Candidate） |
| Phase9_Step44 | v1.0.0 正式发布           |
| Phase9_Step45 | 长期维护（LTS）规划           |

---

# Epic J：未来扩展

| Step          | 名称         |
| ------------- | ---------- |
| Phase9_Step46 | 插件系统规划     |
| Phase9_Step47 | MCP 集成（预留） |
| Phase9_Step48 | 多设备同步（预留）  |
| Phase9_Step49 | 移动端支持（预留）  |
| Phase9_Step50 | 云端协同（预留）   |

---

# Epic K：项目总结

| Step          | 名称                 |
| ------------- | ------------------ |
| Phase9_Step51 | 项目复盘               |
| Phase9_Step52 | 架构复盘               |
| Phase9_Step53 | 性能总结               |
| Phase9_Step54 | 技术成长总结             |
| Phase9_Step55 | 下一版本 Roadmap（v2.0） |

---

# Epic L：最终验收

| Step          | 名称                      |
| ------------- | ----------------------- |
| Phase9_Step56 | 全系统联调                   |
| Phase9_Step57 | 最终 Bug 修复               |
| Phase9_Step58 | 文档最终审查                  |
| Phase9_Step59 | 正式版本归档                  |
| Phase9_Step60 | GrayProject v1.0.0 发布 |

---

# 🎯 Phase9 Milestone（阶段验收）

完成以下内容后，**GrayProject v1.0 正式完成**：

* ✅ 完整的项目文档体系
* ✅ 一键部署与安装能力
* ✅ 完整测试体系（单元、集成、回归、安全）
* ✅ CI/CD 自动化发布流程
* ✅ 良好的产品使用体验
* ✅ 数据备份与迁移能力
* ✅ 完整的 GitHub 项目展示
* ✅ 演示视频、博客和作品集准备完成
* ✅ 发布 **GrayProject v1.0.0**

---

# 🏆 GrayProject v1.0 完整路线图

| Phase   | 名称                 | 核心目标     |
| ------- | ------------------ | -------- |
| Phase 0 | Project Foundation | 建立工程基础   |
| Phase 1 | LLM Core           | 统一模型接口   |
| Phase 2 | RAG                | 构建知识系统   |
| Phase 3 | Memory             | 建立长期记忆   |
| Phase 4 | Tool Calling       | 获得执行能力   |
| Phase 5 | Agent              | 获得自主规划能力 |
| Phase 6 | Automation         | 实现主动运行   |
| Phase 7 | Vision             | 建立多模态感知  |
| Phase 8 | Model              | 构建模型研发体系 |
| Phase 9 | Release            | 产品化与发布   |

---

## PM 最终备注

回顾整个路线，我认为它已经不仅仅是一个“个人 AI 项目”，而是一套**完整的 AI 操作系统工程实践**。

不过，在未来开发过程中，我会坚持两个原则：

1. **路线稳定，细节可优化。** Phase 和主 Step 尽量保持不变，只在必要时拆分子步骤（如 `Phase5_Step18.1`）。
2. **技术跟随发展。** AI 技术更新很快，因此像 MCP、A2A、新的推理框架或模型能力，不会强行塞进主线，而是作为插件或 v2.0 Roadmap 演进。

这样，**GrayProject v1.0** 会是一条清晰、完整、可执行的路线；而 **GrayProject v2.0** 则可以在这个稳定架构上持续扩展，而无需推倒重来。


—————————————————————————————————————————————————————————————————————————————————————————