from pathlib import Path

from flask import Flask, abort, render_template, request, send_file

from agents.html_agent import HtmlAgent
from agents.requirement_agent import RequirementAgent
from project.project_manager import ProjectManager


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

project_manager = ProjectManager()


@app.route("/")
def index():

    projects = project_manager.list_projects()

    return render_template(
        "index.html",
        projects=projects
    )


@app.route("/create", methods=["POST"])
def create():

    requirement = request.form.get(
        "requirement",
        ""
    ).strip()

    if not requirement:

        return "请输入需求内容", 400


    print("\n========== 收到产品需求 ==========")
    print(requirement)
    print("=================================\n")


    print("\n========== 开始生成 PRD ==========\n")

    requirement_agent = RequirementAgent()

    requirement_agent.run(
        requirement
    )

    print("\n========== PRD 生成完成 ==========\n")


    print("\n========== 开始生成 HTML ==========\n")

    html_agent = HtmlAgent()

    html_agent.run()

    print("\n========== HTML 生成完成 ==========\n")


    project_info = project_manager.create_project(
        raw_requirement=requirement
    )

    print("\n========== 历史项目保存完成 ==========")
    print(project_info)
    print("====================================\n")


    return render_template(
        "result.html",
        project=project_info
    )


@app.route("/prd")
def prd():

    path = OUTPUT_DIR / "requirement.md"

    if not path.exists():

        return "暂无 PRD 文件", 404


    content = path.read_text(
        encoding="utf-8"
    )

    return render_template(
        "prd.html",
        content=content,
        project=None
    )


@app.route("/preview")
def preview():

    path = OUTPUT_DIR / "prototype.html"

    if not path.exists():

        return "暂无 HTML 原型", 404


    return send_file(
        path
    )


@app.route("/projects/<project_id>/prd")
def project_prd(project_id):

    project = project_manager.get_project(
        project_id
    )

    if not project:

        abort(404)


    content = project_manager.get_prd(
        project_id
    )

    if content is None:

        return "该项目暂无 PRD 文件", 404


    return render_template(
        "prd.html",
        content=content,
        project=project
    )


@app.route("/projects/<project_id>/preview")
def project_preview(project_id):

    project = project_manager.get_project(
        project_id
    )

    if not project:

        abort(404)


    html_path = project_manager.get_html_path(
        project_id
    )

    if html_path is None:

        return "该项目暂无 HTML 原型", 404


    return send_file(
        html_path
    )


@app.route("/edit")
def edit():

    project_id = request.args.get(
        "project_id",
        ""
    ).strip()

    if not project_id:

        return render_template(
            "index.html",
            projects=project_manager.list_projects()
        )


    project = project_manager.get_project(
        project_id
    )

    if not project:

        abort(404)


    return render_template(
        "index.html",
        projects=project_manager.list_projects(),
        editing_project=project
    )


@app.errorhandler(404)
def not_found(error):

    return """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>页面不存在</title>
    </head>
    <body style="
        padding: 40px;
        font-family: Arial, sans-serif;
    ">
        <h1>页面不存在</h1>
        <p>没有找到对应的项目或文件。</p>
        <a href="/">返回首页</a>
    </body>
    </html>
    """, 404


if __name__ == "__main__":

    print(
        """
==============================
 Product Agent 2.0

 Web 服务启动：

 http://127.0.0.1:5000

==============================
"""
    )

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )