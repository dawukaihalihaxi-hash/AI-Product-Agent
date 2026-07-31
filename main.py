from agents.requirement_agent import RequirementAgent
from agents.html_agent import HtmlAgent
import os



def generate_html_only():

    print("\n========== HTML重新生成模式 ==========\n")


    requirement_path = "output/requirement.md"


    if not os.path.exists(requirement_path):

        print("❌ 没有找到 output/requirement.md")
        print("请先运行新需求生成模式")

        return



    print("========== 已读取现有PRD ==========\n")


    html_agent = HtmlAgent()

    html_agent.run()



    print("\n========== HTML页面生成完成 ==========")
    print("生成文件：output/prototype.html")





def generate_new_project():


    print("\n请输入新的产品需求(输入 END 结束)：\n")


    lines = []


    while True:

        line = input()

        if line.strip().upper() == "END":

            break


        lines.append(line)



    requirement = "\n".join(lines)



    if requirement.strip() == "":

        print("❌ 没有输入任何需求")

        return



    print("\n========== 开始生成PRD ==========\n")



    requirement_agent = RequirementAgent()



    requirement_result = requirement_agent.run(
        requirement
    )



    print("\n========== PRD生成完成 ==========\n")



    print(requirement_result)



    print("\n========== 开始生成HTML原型 ==========\n")



    html_agent = HtmlAgent()


    html_agent.run()



    print("\n========== HTML页面生成完成 ==========")

    print("生成文件：output/prototype.html")







def main():


    print("""
==============================
 Product Agent 1.0
==============================

请选择模式：

1. 新需求 → PRD → HTML（完整流程）

2. 已有PRD → 重新生成HTML

==============================
""")


    choice = input("请输入数字：")



    if choice == "1":


        generate_new_project()



    elif choice == "2":


        generate_html_only()



    else:


        print("❌ 输入错误")





if __name__ == "__main__":

    main()