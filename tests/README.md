# Tests

本目录用于存放 GrayProject 的所有自动化测试。

## 目录说明

### unit/

单元测试。

主要测试：

- 工具函数
- 数据结构
- Agent 内部逻辑
- Memory 模块

---

### integration/

集成测试。

主要测试：

- 多模块协同
- Workflow
- Pipeline

---

### api/

API 测试。

主要包括：

- REST API
- Flask
- FastAPI（未来）
- WebSocket

---

### performance/

性能测试。

包括：

- 推理速度
- Memory 占用
- CPU/GPU 利用率
- Benchmark

---

### fixtures/

测试数据。

例如：

- Mock 数据
- JSON
- Prompt
- 示例文件