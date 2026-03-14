text = input('Enter your text: ')
words = text.split()
for indx in range(len(words)):
    words[indx] = words[indx][::-1]
print("Your results:", ' '.join(words))