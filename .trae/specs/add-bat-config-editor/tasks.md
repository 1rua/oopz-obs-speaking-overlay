# Tasks

- [ ] Task 1: 创建 `configure.bat`（英文配置脚本）
  - [ ] SubTask 1.1: 实现 `config.json` 自动创建逻辑（不存在时从 `config.example.json` 复制）
  - [ ] SubTask 1.2: 实现交互式菜单，列出常用配置项及当前值
  - [ ] SubTask 1.3: 实现用户输入处理，支持修改 string/number/boolean 类型值
  - [ ] SubTask 1.4: 实现配置写回逻辑，使用 Python 内联脚本修改 JSON，保留其他字段
  - [ ] SubTask 1.5: 添加 UTF-8 支持（`chcp 65001`）和中文友好提示

- [ ] Task 2: 创建 `配置设置.bat`（中文入口脚本）
  - [ ] SubTask 2.1: 调用 `configure.bat` 并透传参数

- [ ] Task 3: 修改 `start-overlay.bat`
  - [ ] SubTask 3.1: 启动前检查 `config.json`，不存在则自动复制 `config.example.json`
  - [ ] SubTask 3.2: 在启动信息中增加提示：如需修改配置，请运行 `配置设置.bat`

- [ ] Task 4: 修改 `启动OOPZ OBS叠加层.bat`
  - [ ] SubTask 4.1: 确保透传参数给 `start-overlay.bat` 的调用仍然有效
  - [ ] SubTask 4.2: 确认修改后的 `start-overlay.bat` 已包含配置检查和提示

# Task Dependencies
- Task 2 依赖 Task 1
- Task 4 依赖 Task 3
- Task 3 和 Task 1 可并行
