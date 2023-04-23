import openai
from lr01.conf import Conf


class ChatGPT:

    def __init__(self, conf_path):
        conf = Conf(conf_path)
        openai.api_key = conf.get_chat_gpt_key()

    @staticmethod
    def get_chat_gpt_answer(prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion["choices"][0]["message"]["content"]
