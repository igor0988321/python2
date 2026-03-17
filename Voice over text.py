import pyttsx3

def textToSpeech(text):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + 0.1)

    engine.say(text)
    engine.runAndWait()

textToSpeech(input("Enter the text: "))
