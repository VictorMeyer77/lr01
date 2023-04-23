import gtts
import os
import vlc

OUTPUT_AUDIO_BUFFER_PATH = "resources/output/audio/mouth/buffer.wav"


class Mouth:

    def __init__(self, buffer_path=OUTPUT_AUDIO_BUFFER_PATH, language="fr"):
        self.buffer_path = buffer_path
        self.language = language
        self.player = vlc.MediaPlayer()

    def _convert_text_to_sound(self, text):
        tts = gtts.gTTS(text, lang=self.language)
        tts.save(self.buffer_path)

    def _play_sound(self):
        media = vlc.Media(self.buffer_path)
        self.player.set_media(media)
        self.player.play()
        while self.player.get_state() not in [4, 5, 6, 7]:
            pass

    def run(self, text):
        self._convert_text_to_sound(text)
        self._play_sound()
        os.remove(self.buffer_path)
