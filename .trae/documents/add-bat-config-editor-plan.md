# 为 BAT 增加更改设置功能 — 实施计划

## 项目背景

项目 `oopz-obs-speaking-overlay_V0.2` 是一个 OOPZ OBS 语音叠加层工具，通过 Python HTTP 服务器提供前端页面，展示 OOPZ 语音频道中正在说话的用户。

配置存储在 `config.json` 中，包含服务器地址、叠加层样式、OOPZ 连接参数等。目前已有 `configure.bat` 和 `配置设置.bat`，但功能尚不完善，需要增强以覆盖更多配置项并提升用户体验。

## 当前状态分析

### 已有文件
- `config.json` / `config.example.json`：配置模板，包含 server、overlay、oopz、oopzLocal、mock 等字段
- `configure.bat`：已有一个基础的 Python 内联脚本实现交互式菜单，但只覆盖了 11 个配置项
- `配置设置.bat`：简单调用 `configure.bat`
- `start-overlay.bat`：启动脚本，已有 `config.json` 自动创建逻辑和配置修改提示
- `启动OOPZ OBS叠加层.bat`：中文入口，透传参数给 `start-overlay.bat`

### 现有 `configure.bat` 的问题
1. **配置项不完整**：缺少 `oopzLocal.host`、`oopzLocal.path`、`oopzLocal.reconnectDelaySeconds`、`mock.speakingIntervalMs` 等常用配置
2. **mock 用户管理缺失**：无法添加/删除/修改 mock 模式下的模拟用户
3. **用户体验待提升**：菜单没有分类，修改后没有显示变更对比
4. **缺少输入验证**：例如 `layout` 只接受 `horizontal/vertical/grid`，但脚本没有验证

## 实施步骤

### Step 1: 增强 `configure.bat` 的交互式配置菜单

**目标**：重写 `configure.bat` 中的 Python 内联脚本，提供更完整的配置编辑功能。

**具体修改**：
1. **扩展配置项列表**，增加以下项目：
   - `oopzLocal.host` — OOPZ 本地 WebSocket 地址
   - `oopzLocal.path` — OOPZ 本地 WebSocket 路径
   - `oopzLocal.reconnectDelaySeconds` — 重连延迟秒数
   - `mock.speakingIntervalMs` — Mock 模式说话切换间隔

2. **增加 mock 用户管理子菜单**：
   - 列出当前 mock.users 列表
   - 支持添加新用户（输入 id、displayName、avatarUrl）
   - 支持删除用户
   - 支持修改已有用户的 displayName 和 avatarUrl

3. **增加输入验证**：
   - `overlay.layout` 只允许 `horizontal`、`vertical`、`grid`
   - `oopz.mode` 只允许 `oopz-local`、`mock`
   - `overlay.showIds`、`overlay.showDisplayNames` 只允许 `true`/`false`
   - 数值类型（port、avatarSize、dimOpacity 等）验证范围合理性

4. **优化菜单展示**：
   - 按类别分组显示（服务器设置、叠加层样式、OOPZ 连接、Mock 设置）
   - 修改成功后显示旧值 → 新值的对比
   - 增加返回上级菜单的选项

### Step 2: 验证 `start-overlay.bat` 的现有功能

**目标**：确认 `start-overlay.bat` 已满足 spec 要求。

**检查项**：
- [x] 启动前检查 `config.json`，不存在则自动复制 `config.example.json`
- [x] 启动信息中包含配置修改提示（"如需修改配置，请运行 '配置设置.bat'"）

**结论**：`start-overlay.bat` 已满足 spec 要求，无需修改。

### Step 3: 验证 `启动OOPZ OBS叠加层.bat` 的现有功能

**目标**：确认中文入口脚本仍正确透传参数。

**检查项**：
- [x] `call ".\start-overlay.bat" %*` 能正确透传所有参数

**结论**：无需修改。

### Step 4: 验证 `配置设置.bat` 的现有功能

**目标**：确认中文入口脚本正确调用 `configure.bat`。

**检查项**：
- [x] `call ".\configure.bat" %*` 能正确调用并透传参数

**结论**：无需修改。

### Step 5: 测试与验证

**测试场景**：
1. 双击 `配置设置.bat`，验证菜单正确显示所有配置项
2. 修改 `server.port` 为其他值，验证写回 `config.json` 成功
3. 修改 `overlay.layout` 为无效值，验证被拒绝并提示允许的值
4. 在 mock 用户管理中添加/删除用户，验证 `config.json` 正确更新
5. 删除 `config.json` 后运行 `配置设置.bat`，验证自动从 `config.example.json` 创建
6. 运行 `start-overlay.bat`，验证配置检查和提示信息正常

## 文件变更清单

| 文件 | 操作 | 说明 |
|------|------|------|
| `configure.bat` | 修改 | 增强交互式配置菜单，扩展配置项，增加验证和 mock 用户管理 |
| `配置设置.bat` | 无需修改 | 已正确调用 `configure.bat` |
| `start-overlay.bat` | 无需修改 | 已满足 spec 要求 |
| `启动OOPZ OBS叠加层.bat` | 无需修改 | 已正确透传参数 |
| `config.example.json` | 无需修改 | 保持作为默认模板 |

## 风险与注意事项

1. **编码问题**：BAT 文件使用 `chcp 65001` 确保 UTF-8，Python 内联脚本也需指定 `encoding="utf-8"`
2. **JSON 格式保留**：修改 `config.json` 时必须保留原有字段和缩进格式，使用 `json.dump` 的 `indent=2`
3. **类型安全**：用户输入的字符串需要正确解析为 bool/int/float，避免类型错误导致后端读取失败
4. **mock 用户数组操作**：添加/删除用户时需确保 JSON 数组结构正确，不破坏其他字段
