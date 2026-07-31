# AI Product Agent 🚀

An open-source AI Product Manager Assistant that transforms natural language requirements into structured PRDs and interactive HTML prototypes.
一个基于大语言模型（LLM）的 AI 产品经理助手，可以帮助产品经理、设计师和开发者，将自然语言需求自动转换为产品需求文档（PRD）以及可预览的 HTML 产品原型。

## 📌 Overview

AI Product Agent 使用多个 AI Agent 协同工作，将这个流程自动化：

Natural Language Requirement
    ↓
Requirement Agent
    ↓
Product Requirement Document (PRD)
    ↓
HTML Prototype Agent
    ↓
Interactive Prototype

目标是降低产品经理、设计师和开发人员之间的信息沟通成本，让产品想法能够快速转化为可视化产品方案。
---

## Project History Management

用户可以：
- 查看历史需求
- 查看历史 PRD
- 查看历史原型
- 基于已有项目继续优化

## 🏗 Architecture

            User
             ↓
      Web Interface
             ↓
    Requirement Agent
             ↓
          PRD
             ↓
        HTML Agent
             ↓
    Prototype Generator
             ↓
    Project Manager
---

# 📂 Project Structure
AI-Product-Agent
│
├── agents
│ ├── requirement_agent.py
│ └── html_agent.py
│
├── project
│ ├── project_manager.py
│ └── init.py
│
├── prompts
│ ├── requirement.txt
│ └── html.txt
│
├── templates
│ ├── index.html
│ └── prd.html
│
├── static
│
├── app.py
├── llm.py
├── config.py
│
├── requirements.txt
├── README.md
└── LICENSE

---
# ⚙️ Installation
1. Clone Repository
```bash
git clone https://github.com/your-username/AI-Product-Agent.git
cd AI-Product-Agent

2. Install Dependencies
pip install -r requirements.txt

3. Configure API Key
本项目需要连接大语言模型 API（替换config文件）

API_KEY=your_api_key
BASE_URL=your_model_api_endpoint
MODEL=your_model_name

4. 浏览器访问：
http://127.0.0.1:5000
