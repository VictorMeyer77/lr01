import speech_recognition as sr
import copy
import time


class Ear:

    def __init__(self, language="fr"):

        self.memory = {}
        self.language = language

    def listen(self):
        recognizer = sr.Recognizer()
        while True:
            try:
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                    text = recognizer.recognize_google(audio, language=self.language)
                    self.memory[time.time()] = text
            except sr.exceptions.UnknownValueError:
                continue

    def get_memory(self):
        memory_to_return = copy.deepcopy(self.memory)
        memory_str = " ".join(memory_to_return.values())
        [self.memory.pop(key) for key in memory_to_return.keys()]
        return memory_str



a = Ear()


import threading

x = threading.Thread(target=a.listen)

x.start()

while True:

    mem = a.get_memory()
    if mem != "":
        print(mem)
    time.sleep(1)