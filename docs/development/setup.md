# GrayProject Development Setup

## 1. Overview

本文档记录 GrayProject 的开发环境配置。

目标：

- 保证开发环境可复现
- 降低环境迁移成本
- 为后续 AI 模型实验提供统一基础

---

# 2. Hardware Environment

## Development Machine

主要开发设备：

- GPU: NVIDIA RTX 5060 Laptop GPU   8G
- CPU: AMD Ryzen 9 8940HX with Radeon Graphics         (2.40 GHz)
- Memory: 16.0 GB (15.2 GB 可用)
- Storage: 1T

GPU主要用于：

- 本地模型推理
- 小规模模型训练实验
- 深度学习算法测试


---

# 3. Operating System

当前主要开发环境：

- Windows 11

未来支持：

- Ubuntu Linux

Linux环境主要用于：

- 深度学习训练
- CUDA环境测试
- 服务器部署


---

# 4. Python Environment

Python版本：3.11

推荐使用虚拟环境：

```bash
python -m venv .venv


启动：

Windows:
.venv\Scripts\activate

Linux:
source .venv/bin/activate