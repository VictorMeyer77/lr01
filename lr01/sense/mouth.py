import gtts
import pygame
import os

OUTPUT_AUDIO_BUFFER_PATH = "resources/output/audio/mouth/buffer.wav"


class Mouth:

    def __init__(self, buffer_path=OUTPUT_AUDIO_BUFFER_PATH, language="fr"):
        self.buffer_path = buffer_path
        self.language = language
        pygame.init()

    def _convert_text_to_sound(self, text):
        tts = gtts.gTTS(text, lang=self.language)
        tts.save(self.buffer_path)

    def _play_sound(self):
        audio = pygame.mixer.Sound(self.buffer_path)
        channel = audio.play()
        while channel.get_busy():
            pygame.time.wait(100)

    def run(self, text):
        self._convert_text_to_sound(text)
        self._play_sound()
        os.remove(self.buffer_path)
