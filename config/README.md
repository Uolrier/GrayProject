# Config

本目录用于统一管理 GrayProject 的所有配置。

## Python 配置

- settings.py：统一配置入口
- development.py：开发环境配置
- production.py：生产环境配置
- paths.py：项目路径
- constants.py：公共常量

## YAML 配置

- llm.yaml：大语言模型
- embedding.yaml：Embedding 模型
- database.yaml：数据库
- vectordb.yaml：向量数据库
- logging.yaml：日志
- system.yaml：系统配置

后续所有模块应通过统一配置接口读取配置，不应在业务代码中硬编码参数。