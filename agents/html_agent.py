import os
import re

from llm import LLM


class HtmlAgent:

    def __init__(self):
        self.llm = LLM()


    def clean_html(self, content):

        """
        清理模型输出
        """

        # 去除 Markdown代码块
        content = content.replace("```html", "")
        content = content.replace("```", "")

        content = content.strip()


        # 截取DOCTYPE开始的位置
        start = content.find("<!DOCTYPE")

        if start != -1:
            content = content[start:]


        # 截取html结束位置
        end = content.rfind("</html>")

        if end != -1:
            content = content[:end + 7]


        return content



    def validate_html(self, content):

        """
        HTML完整性检查
        """

        checks = {

            "DOCTYPE": "<!DOCTYPE" in content,

            "html开始": "<html" in content,

            "body开始": "<body" in content,

            "body结束": "</body>" in content,

            "html结束": "</html>" in content

        }


        print("\n========== HTML检查 ==========")

        for key, value in checks.items():

            print(
                f"{key}: {'通过' if value else '失败'}"
            )


        return all(checks.values())



    def run(self):


        # 读取需求文档

        requirement_path = "output/requirement.md"


        if not os.path.exists(requirement_path):

            raise Exception(
                "没有找到 output/requirement.md，请先生成需求文档"
            )


        with open(
            requirement_path,
            "r",
            encoding="utf-8"
        ) as f:

            requirement = f.read()



        # 读取HTML Prompt

        with open(
            "prompts/html.txt",
            "r",
            encoding="utf-8"
        ) as f:

            prompt = f.read()



        final_prompt = f"""
{prompt}


========================

产品需求文档：

{requirement}

========================

再次提醒：

只输出完整HTML。

必须包含：

<!DOCTYPE html>

<html>

<head>

<body>

</body>

</html>

不要输出解释。
"""



        print(
            "========== HTML Agent =========="
        )


        # 调用模型

        result = self.llm.chat(final_prompt)



        # 清理

        html = self.clean_html(result)



        # 检查

        if not self.validate_html(html):

            print(
                "\n❌ HTML生成失败，未保存文件"
            )

            return html



        # 创建目录

        os.makedirs(
            "output",
            exist_ok=True
        )


        output_path = (
            "output/prototype.html"
        )



        # 保存

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(html)



        print(
            f"\n✅ HTML 已保存：{output_path}"
        )


        print(
            f"文件大小：{os.path.getsize(output_path)} bytes"
        )


        return html
