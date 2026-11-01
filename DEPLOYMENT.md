# Product Agent 线上演示部署

本目录是独立部署副本。本地原项目仍位于 `/Users/k.paris/product_agent/2.0`，`python3 app.py` 和 `http://127.0.0.1:5001` 保留。

## Render 免费 Web Service

- 代码：本目录单独上传私有 GitHub 仓库。不上传原仓库、历史项目、备份、会话密钥或本地 config.py。
- Python 3.12.10；安装：`pip install -r requirements.txt`。
- 启动：`gunicorn -c gunicorn.conf.py wsgi:app`。
- 选择 Free 方案。健康检查路径 `/healthz`。
- 环境变量：`MODEL_API_KEY`（模型密钥）、`PRODUCT_AGENT_SECRET_KEY`（固定随机会话密钥）、`PRODUCT_AGENT_ACCESS_PASSWORD`（演示访问口令）。不要把密钥写入代码或提交到 GitHub。
- 可选环境变量：`MODEL_BASE_URL`、`MODEL_NAME`，未设置则使用现有模型服务的地址和模型名称。
- 浏览器提示登录时，用户名可填 `demo`，密码填写演示访问口令。
- 使用一个进程、多个请求线程，避免多个进程错误地将彼此的后台任务判为中断。
- 线上不启用 Flask 调试服务；本地入口不变。

## 演示限制

免费实例闲置后休眠，打开时可能需要等待唤醒。运行时项目和任务记录存放在临时磁盘，休眠、重启或重新部署后可能丢失。本地历史记录不受影响。线上生成的重要结果需要及时下载。此方案没有承诺永久历史存储或本地线上自动同步。

模型调用仍由模型服务计费和限流；免费托管并不意味着模型调用免费。免费实例不能保证不中断长任务，适合演示。

## Figma

下载 JSON 和插件不变；导入仍使用 Figma 桌面端的本地插件。部署网页不会将本地开发插件变成 Figma 网页端插件。
