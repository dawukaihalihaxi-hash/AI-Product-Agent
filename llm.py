import requests

from config import API_KEY, BASE_URL, MODEL


class LLM:

    def __init__(self):

        self.api_key = API_KEY
        self.base_url = BASE_URL
        self.model = MODEL


    def chat(self, prompt):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }


        payload = {

            "model": self.model,

            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            # 降低随机性，让HTML输出更稳定
            "temperature": 0.2,

            # 限制最大输出长度
            # 防止生成HTML时无限扩展
            "max_tokens": 30000
        }


        response = requests.post(

            self.base_url,

            headers=headers,

            json=payload,

            # 保留较长等待时间
            timeout=600
        )


        if response.status_code != 200:

            raise Exception(
                f"API调用失败: {response.status_code}\n{response.text}"
            )


        result = response.json()


        return result["choices"][0]["message"]["content"]