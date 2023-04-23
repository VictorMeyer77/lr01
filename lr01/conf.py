import os


class Conf:

    def __init__(self, conf_dir_path):
        self.conf_dir_path = conf_dir_path

    def get_chat_gpt_key(self):
        with open(os.path.join(self.conf_dir_path, "chatgpt.key"), "r") as file:
            return file.readlines()[0].replace("\n", "")
