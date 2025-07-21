from googletrans import Translator, LANGUAGES
from gtts import gTTS
import pygame
import os

translator = Translator()

language_options = LANGUAGES.items()
language_codes = []
language_names = []

def errors():
    print('Unknown Language. Wisely choose from this:')
    print(f"Language Codes: {language_codes}\n")
    print(f"Language Names: {language_names}\n")

for code, name in language_options:
    language_codes.append(code)
    language_names.append(name.lower())

def get_language_code(language):
    if language in language_codes:
        return language
    elif language in language_names:
        return language_codes[language_names.index(language)]
    else:
        return None

translating_from = input("Enter the language you want to translate from: ").lower()
word = input('Enter the word or phrase to translate: ').lower()
translating_to = input("Enter the language you want to translate to: ").lower()

translating_from_code = get_language_code(translating_from)
translating_to_code = get_language_code(translating_to)

def is_valid_language(language_code):
    return language_code in language_codes

try:
    if is_valid_language(translating_from_code) and is_valid_language(translating_to_code):
        translation = translator.translate(word, src=translating_from_code, dest=translating_to_code).text
        print(f"Translation: {translation.capitalize()}")
        
        # Convert text to speech
        tts = gTTS(text=translation, lang=translating_to_code)
        audio_file = "translated.mp3"
        tts.save(audio_file)
        
        # Initialize pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Clean up the audio file
        pygame.mixer.quit()
        os.remove(audio_file)
    else:
        errors()
except Exception as e:
    print("Something went wrong:", e)
    errors()