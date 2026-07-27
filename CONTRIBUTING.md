# Contributing Guide

## 1. 项目贡献流程

所有代码、文档、实验记录的修改，需要遵循以下流程：

1. 创建或修改对应功能分支
2. 完成开发与测试
3. 更新相关文档
4. 提交 Git Commit
5. 合并到主分支


## 2. Git 分支规范

主分支：

- main

开发分支：

- dev

功能分支：

格式：

feature/功能名称

例如：

feature/memory-system
feature/local-model


修复分支：

bugfix/问题名称


## 3. Commit规范

Commit格式：

类型: 内容描述


类型包括：

feat:
新增功能

fix:
修复问题

docs:
文档修改

refactor:
代码重构

test:
测试相关

chore:
工程配置修改


示例：

feat: add local file parser

docs: update architecture document


## 4. Pull Request原则

提交合并前需要确认：

- 功能是否完成
- 文档是否同步
- 是否影响已有模块
- 是否通过基础测试


## 5. 文档维护

涉及架构变化时，需要同步修改：

docs/architecture.md

涉及重大技术选择时，需要记录：

docs/decisions.md