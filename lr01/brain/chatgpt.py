import openai


class ChatGPT:

    def __init__(self, conf):
        openai.api_key = conf.get_chat_gpt_key()

    @staticmethod
    def get_chat_gpt_answer(prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion["choices"][0]["message"]["content"]
