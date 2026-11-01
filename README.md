# AI Product Agent · 产品经理助手 2.0

将自然语言需求生成配套的 **PRD、可交互 HTML 原型和 Workflow**，支持历史版本管理、继续优化、Figma 可编辑图层导出，以及中断任务的断点续生成。

[在线演示](https://product-agent-kparis.onrender.com/)（需要演示访问口令）。本地与线上独立运行，本地入口保留为 `http://127.0.0.1:5001`。

## 功能与使用流程

1. 首页输入需求，后台依次生成 PRD → HTML 原型 → Workflow → 配套校验，完成后保存为项目。
2. 查看 PRD、预览原型、查看 Workflow；Workflow 支持下载 SVG 和可在 diagrams.net 继续编辑的 `.drawio` 文件。
3. 从历史项目点击“继续优化”，基于已有需求、PRD 和原型生成三份配套内容。查看结果后选择另存新版本，或确认覆盖原版；覆盖前保留备份。
4. 模型限流、超时或服务中断时保留任务和已完成阶段。通过首页独立的“未完成与待确认的任务”入口查看、下载已有成果，并点击“继续生成”补齐剩余步骤。
5. 待完成任务分别展示累计用时、完成情况和失败原因／错误代码；支持停止任务、二次确认后删除。已保存的历史项目独立管理，支持重命名和删除。
6. 导出原始 HTML，或通过“导出 Figma”生成 JSON，再使用附带的 Product Agent Importer 插件导入可编辑图层。

## 最新版源码

完整的 2.0 源码、测试、Figma 插件和运行配置在 [product-agent-2.0.zip](product-agent-2.0.zip) 中。解压后为 `2.0/` 目录。仓库早期目录保留作历史参考，运行最新版请使用此源码包。

## 本地运行

需要 Python 3.12 或以上版本。

```bash
git clone https://github.com/dawukaihalihaxi-hash/AI-Product-Agent.git
cd AI-Product-Agent
unzip product-agent-2.0.zip
cd 2.0
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export MODEL_API_KEY='填写自己的模型密钥'
python3 app.py
```

打开 http://127.0.0.1:5001 。配置通过环境变量读取，不需要把密钥写入代码。可选配置：`MODEL_NAME`、`MODEL_BASE_URL`、`PRODUCT_AGENT_SECRET_KEY`。`.env.example` 仅供参考，不会自动加载；本机项目记录和会话文件不提交到仓库。

## Figma 导入

在“导出 Figma”页生成并下载最新 JSON，下载并解压导入插件。Figma 桌面端通过 **Plugins → Development → Import plugin from manifest…** 加载 `figma-plugin/manifest.json`，运行 Product Agent Importer，选择 JSON 并点击“导入为可编辑图层”。JSON 和 HTML 都不能当作 `.fig` 原生文件直接打开。

转换尽可能保留文字、图形、按钮、表单外观、布局及可识别页面跳转。复杂 CSS、字体、媒体、输入行为和业务逻辑不能保证完整转换，页面和插件会展示转换限制；原始 HTML 继续保留交互。非截图导出。

## 架构

- `agents/requirement_agent.py`：生成和优化 PRD。
- `agents/html_agent.py`：生成和优化原型。
- `agents/workflow_agent.py`：从 PRD 和原型提取配套业务流程。
- `workflow_document.py`：流程校验、SVG／draw.io 导出及三份产物一致性校验。
- `refinement_jobs.py`：后台任务、重试、阶段检查点、恢复、取消和删除。
- `project/project_manager.py`：项目存储、版本保存、覆盖和备份。
- `templates/`、`static/`：页面与浏览器端导出逻辑。
- `figma-plugin/`：创建 Figma 原生设计节点及可识别的交互。

## 验证

```bash
python3 -m unittest discover -s tests -q
node tests/test_task_delete.cjs
```

当前后端自动化测试 78 项通过，模型调用使用模拟结果；这不代表所有真实模型输出或所有 HTML 样式都能无损转换。

## 部署与边界

[部署说明](DEPLOYMENT.md) · [产品工作流说明](WORKFLOW.md)

云端使用单进程、多线程的 Gunicorn，密钥和访问口令在平台环境变量中管理。免费实例使用临时磁盘，重启或重新部署可能清空线上记录。断点续生成需要任务文件仍在同一存储中；未使用永久磁盘时不能承诺跨部署恢复。模型使用仍可能计费或限流。
