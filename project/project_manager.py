import json
import shutil

from datetime import datetime
from pathlib import Path



class ProjectManager:


    def __init__(self):

        # project_manager.py 在：
        # 2.0/project/project_manager.py
        #
        # 所以 parent.parent 才是：
        # 2.0/

        self.base_dir = (
            Path(__file__)
            .resolve()
            .parent
            .parent
        )


        # 当前生成文件目录

        self.output_dir = (
            self.base_dir
            /
            "output"
        )


        # 历史项目目录

        self.projects_dir = (
            self.base_dir
            /
            "project"
            /
            "projects"
        )


        self.projects_dir.mkdir(
            parents=True,
            exist_ok=True
        )




    def create_project(
        self,
        raw_requirement,
        project_name=None
    ):


        if not raw_requirement.strip():

            raise ValueError(
                "需求不能为空"
            )



        if not project_name:


            first_line = (
                raw_requirement
                .splitlines()[0]
                .strip()
            )


            project_name = (
                first_line[:30]
                if first_line
                else "未命名项目"
            )



        project_id = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )



        project_dir = (
            self.projects_dir
            /
            project_id
        )



        project_dir.mkdir(
            parents=True,
            exist_ok=True
        )



        # 当前输出文件

        current_prd = (
            self.output_dir
            /
            "requirement.md"
        )


        current_html = (
            self.output_dir
            /
            "prototype.html"
        )



        has_prd = False

        has_html = False




        # 保存PRD

        if current_prd.exists():

            shutil.copy2(
                current_prd,
                project_dir
                /
                "requirement.md"
            )

            has_prd = True




        # 保存HTML

        if current_html.exists():

            shutil.copy2(
                current_html,
                project_dir
                /
                "prototype.html"
            )

            has_html = True





        # 保存原始输入需求

        with open(
            project_dir / "raw_requirement.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                raw_requirement
            )





        now = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )



        info = {


            "id":
            project_id,


            "name":
            project_name,


            "created_at":
            now,


            "updated_at":
            now,


            "has_prd":
            has_prd,


            "has_html":
            has_html

        }





        with open(
            project_dir / "info.json",
            "w",
            encoding="utf-8"
        ) as f:


            json.dump(
                info,
                f,
                ensure_ascii=False,
                indent=2
            )




        return info






    def list_projects(self):


        projects = []



        if not self.projects_dir.exists():

            return projects




        for item in self.projects_dir.iterdir():


            if not item.is_dir():

                continue



            info_file = (
                item
                /
                "info.json"
            )



            if not info_file.exists():

                continue




            with open(
                info_file,
                "r",
                encoding="utf-8"
            ) as f:


                projects.append(
                    json.load(f)
                )




        projects.sort(
            key=lambda x:
            x.get(
                "created_at",
                ""
            ),
            reverse=True
        )



        return projects






    def get_project(
        self,
        project_id
    ):


        info_file = (

            self.projects_dir
            /
            project_id
            /
            "info.json"

        )


        if not info_file.exists():

            return None



        with open(
            info_file,
            "r",
            encoding="utf-8"
        ) as f:


            return json.load(f)







    def get_prd(
        self,
        project_id
    ):


        file = (

            self.projects_dir
            /
            project_id
            /
            "requirement.md"

        )


        if not file.exists():

            return None



        return file.read_text(
            encoding="utf-8"
        )







    def get_html_path(
        self,
        project_id
    ):


        file = (

            self.projects_dir
            /
            project_id
            /
            "prototype.html"

        )


        if not file.exists():

            return None



        return file
