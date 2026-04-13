import pyttsx3

engine = pyttsx3.init()
text = input("Enter your message: ")
engine.say(text)
engine.runAndWait()
