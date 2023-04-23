from brain.chatgpt import ChatGPT
from conf import Conf
from sense.ear import Ear
from sense.mouth import Mouth

CONF_PATH = "conf"

conf = Conf(CONF_PATH)
ear = Ear()
mouth = Mouth()
chat_gpt = ChatGPT(conf)

while True:

    ear.listen()
    words_heard = ear.get_memory()
    if words_heard != "":
        answer = chat_gpt.get_chat_gpt_answer(words_heard)
        mouth.run(answer)
