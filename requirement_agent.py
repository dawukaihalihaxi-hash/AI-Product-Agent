import os

from llm import LLM


class RequirementAgent:

    def __init__(self):
        self.llm = LLM()


    def run(self, user_requirement):

        print("========== Requirement Agent ==========")

        # 读取需求分析 Prompt
        with open(
            "prompts/requirement.txt",
            "r",
            encoding="utf-8"
        ) as f:

            prompt = f.read()


        final_prompt = f"""
{prompt}


========================

用户需求：

{user_requirement}
"""


        # 调用大模型
        result = self.llm.chat(final_prompt)


        # 创建输出目录
        os.makedirs(
            "output",
            exist_ok=True
        )


        # 保存 PRD
        output_file = "output/requirement.md"


        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(result)


        print(f"✅ 已保存到：{output_file}")


        return result