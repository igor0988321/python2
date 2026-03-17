from deep_translator import GoogleTranslator



text = input("Enter the text: ")

translation = GoogleTranslator( src='ru',dest='en').translate(text)
print(translation)