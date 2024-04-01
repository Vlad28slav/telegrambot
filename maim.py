from gtts import gTTS

language ='en'
TLd = 'us'

def convert_to_sound(text : str):
    tts = gTTS(text, lang= language, tld=TLd)
    sound = 'sound.ogg'
    tts.save(sound)