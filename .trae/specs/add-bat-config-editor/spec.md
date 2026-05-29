# 为 BAT 增加更改设置功能 Spec

## Why
当前项目通过 `config.json` / `config.example.json` 管理配置，用户必须手动编辑 JSON 文件才能修改叠加层参数（如布局、头像大小、透明度等）。这对于不熟悉 JSON 的普通用户不够友好。需要为现有的 BAT 启动脚本增加一个交互式配置编辑功能，让用户可以通过简单的命令行菜单直接修改常用设置。

## What Changes
- 新增 `configure.bat` / `配置设置.bat`：提供交互式命令行菜单，列出常用配置项并允许用户输入新值，最后将修改写回 `config.json`。
- 修改 `start-overlay.bat` 和 `启动OOPZ OBS叠加层.bat`：启动前检测是否存在 `config.json`，若不存在则自动从 `config.example.json` 复制一份，并提示用户可通过 `配置设置.bat` 修改。
- 保持 `config.example.json` 不变，作为默认模板。
- 编辑功能仅覆盖 `config.json` 中已存在的字段，不删除其他字段，保留用户自定义扩展。

## Impact
- 新增文件：`configure.bat`、`配置设置.bat`
- 修改文件：`start-overlay.bat`、`启动OOPZ OBS叠加层.bat`
- 受影响能力：用户启动流程、配置管理体验

## ADDED Requirements
### Requirement: 交互式配置编辑
The system SHALL provide a Windows Batch script that allows users to edit common overlay settings via an interactive command-line menu.

#### Scenario: 成功修改配置
- **WHEN** 用户双击 `配置设置.bat` 或 `configure.bat`
- **THEN** 脚本显示当前 `config.json` 中的常用配置项（如 host、port、layout、avatarSize、dimOpacity、inactiveGrayscale、highlightScale、showIds、showDisplayNames、mode、oopzLocal.port）
- **AND** 用户输入选项编号选择要修改的项
- **AND** 用户输入新值
- **AND** 脚本将新值写回 `config.json`，保留其他字段不变
- **AND** 脚本提示修改成功并返回菜单

#### Scenario: 无 config.json 时自动创建
- **WHEN** 用户运行配置脚本但目录下没有 `config.json`
- **THEN** 脚本自动从 `config.example.json` 复制一份为 `config.json`
- **AND** 提示用户已创建默认配置，可以继续编辑

#### Scenario: 启动脚本自动检查配置
- **WHEN** 用户运行 `start-overlay.bat` 或 `启动OOPZ OBS叠加层.bat`
- **THEN** 脚本检查 `config.json` 是否存在
- **AND** 若不存在，自动从 `config.example.json` 复制
- **AND** 提示用户可通过 `配置设置.bat` 修改配置

## MODIFIED Requirements
### Requirement: 启动流程
[Complete modified requirement]
- 启动脚本在启动 Python 服务前，自动确保 `config.json` 存在。
- 启动脚本在标题或提示信息中增加一行说明：如需修改配置，请运行 `配置设置.bat`。

## REMOVED Requirements
无
