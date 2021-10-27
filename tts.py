#!/usr/bin/env python
#################### START IMPORTS ####################
import config
import pyttsx3
import time
import random
#################### END IMPORTS ####################

#################### START CONSTANTS ####################
TIME_BETWEEN_TTS_LOWER = config.time_between_tts_phrases_lower
TIME_BETWEEN_TTS_UPPER = config.time_between_tts_phrases_upper
TTS_PHRASES_AND_WEIGHTS_MAP = config.tts_phrases_and_weights
PHRASES = list(TTS_PHRASES_AND_WEIGHTS_MAP.keys())
WEIGHTS = list(TTS_PHRASES_AND_WEIGHTS_MAP.values())
ENGINE = pyttsx3.init()
#################### END CONSTANTS ####################

#################### START HELPERS ####################
def say_phrase(phrase):
    ENGINE.say(phrase)
    ENGINE.runAndWait()
    time.sleep(get_random_time_between_tts())

def get_random_time_between_tts():
    """
    Chooses a random amount of time between TTS phrases between [lower, upper] inclusive,
    defined in config.py.
    """
    return random.randint(TIME_BETWEEN_TTS_LOWER, TIME_BETWEEN_TTS_UPPER)

def get_random_phrase():
    """
    Chooses a random phrase from the list of phrases defined in config.py, 
    based on the weight probabilities defined.
    """
    return random.choices(PHRASES, WEIGHTS, k=1)[0]
#################### END HELPERS ####################

#################### MAIN ####################
def main():
    # Runs forever until the program is terminated (CTRL+Z)
    while True:
        say_phrase(get_random_phrase())

if __name__ == "__main__":
    main()
#################### END MAIN ####################