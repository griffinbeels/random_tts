# EDIT ME TO CHANGE WHAT THE TTS VOICE CAN SAY ALONG WITH THE PROBABILITIES.
# The phrases that can be said are defined in quotes.
# For each phrase, the associated number is the weight for that phrase.
# A higher number means a higher chance of showing up; lower means less likely.
tts_phrases_and_weights = {
    "only normals" : 1,
    "only special moves" : 1,
    "back off" : 1,
    "use burst" : 1,
    "drop your next combo" : 1,
    "roman cancel" : 1,
    "mash" : 1,
    "stop moving" : 1
}

# EDIT ME TO CHANGE THE AMOUNT OF TIME BETWEEN PHRASES.
# The time between phrases will be a random number 
# between [lower, upper] inclusive.
time_between_tts_phrases_lower = 5
time_between_tts_phrases_upper = 10